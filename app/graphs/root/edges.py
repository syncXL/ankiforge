from ...models import root
from langgraph.types import Send
from langgraph.graph import END

def produce_more_card(deck_state: root.DeckState):
    assessments_left = deck_state["no_of_cards"] - len(deck_state.get('assessments',[]))
    if assessments_left != 0:
        deck_state["batch_size"] = min(assessments_left, 10)
        return [Send("generate_assessments", deck_state)]
    return END


def distribute_cards(deck_state: root.DeckState):
    last_batch = deck_state["assessments"][-deck_state["batch_size"]:]
    existing_tags = deck_state.get("tags",[])
    deck_name = deck_state["deck_name"]
    sub_deck_name = deck_state.get("subdeck_name","")
    payload = []
    for card in last_batch:
        state= root.CardState(
            raw_card=card,
            existing_tags=existing_tags,
            deck_name=deck_name,
            subdeck_name=sub_deck_name)
        req = Send("format_card",state )
        payload.append(req)
    return payload