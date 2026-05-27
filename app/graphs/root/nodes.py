from pathlib import Path
from langchain_core.messages import HumanMessage, AIMessage
from ...models import root
from ... import dependencies
import fitz

def extract_pdf_pages(card_state : root.DeckState) -> root.DeckState:
    filepath = card_state["filepath"]
    path = Path(filepath)
    start_page = card_state["start_page"]
    end_page = card_state["end_page"]

    if path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported")

    doc = fitz.open(path)

    if start_page < 0:
        start_page = 0

    if end_page == -1:
        end_page = len(doc) - 1
    else:
        end_page = min(end_page, len(doc) - 1)

    if start_page > end_page:
        raise ValueError("start_page must be less than or equal to end_page")

    pages_text = []
    for page_num in range(start_page, end_page + 1):
        page = doc.load_page(page_num)
        pages_text.append(page.get_text())

    return {"content" : "\n".join(pages_text)}

async def estimate_cards(card_state : root.DeckState) -> root.DeckState:
    instruction = dependencies.read_text("estimator.md", resources=card_state["content"])
    llm = dependencies.get_heavy_llm()
    full_instruction = AIMessage(content=instruction)
    number_of_cards = await llm.ainvoke([full_instruction])
    total_cards = int(number_of_cards.text)
    return {"no_of_cards" : total_cards}

async def plan_card(card_state: root.DeckState) -> root.DeckState:
    llm = dependencies.get_heavy_llm()
    card_types = ["basic", "basic_reversed", "cloze"]
    card_docs = []
    for card in card_types:
        doc = dependencies.read_text(f"types/{card}.md")
        card_docs.append(doc)
    card_docs = "\n".join(card_docs)
    existing_assessments= card_state.get("assessments",[])
    generator = dependencies.read_text(
        "generator.md",
        assessment_desc=card_docs,
        resources=card_state["content"],
        existing_assessments="\n".join(existing_assessments),
        no_of_assessments=card_state["batch_size"]
    )

    instruction = HumanMessage(content=generator)
    output = await llm.ainvoke([instruction], schema=root.Cards)
    output = output.assessments
    return {"assessments" : output}


async def format_card(card_state : root.CardState):
    llm = dependencies.get_max_llm()
    ankiClient = dependencies.get_anki_loader()
    existing_tags = card_state.get("existing_tags",[])
    raw_card = card_state["raw_card"]
    existing_tags_str = "\n".join(existing_tags) if len(existing_tags) > 0 else "None yet"
    
    prompt = dependencies.read_text(
        "formatter.md",
        raw_card=raw_card,
        existing_tags=existing_tags_str
    )
    response = await llm.ainvoke([HumanMessage(content=prompt)], schema=root.FormattedCard)
    card = response.card
    print(f"Pushing: {card.model_dump()}")
    await ankiClient.push_card(card=response.card, deck_name=card_state["deck_name"],subdeck_name=card_state.get("subdeck_name",""))
    return None
