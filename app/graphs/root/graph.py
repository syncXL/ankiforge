from langgraph.graph import StateGraph, START, END
from ...models import root
from . import nodes
from . import edges

def compile_graph_schema():
    graph = StateGraph(root.DeckState)
    graph.add_node("extract_content", nodes.extract_pdf_pages)
    graph.add_node("estimate_n_cards", nodes.estimate_cards)
    graph.add_node("generate_assessments", nodes.plan_card)
    graph.add_node("format_card", nodes.format_card)

    graph.add_edge(START, "extract_content")
    graph.add_edge("extract_content", "estimate_n_cards")
    graph.add_conditional_edges("estimate_n_cards", edges.produce_more_card)
    graph.add_conditional_edges("generate_assessments", edges.distribute_cards)
    graph.add_conditional_edges("generate_assessments", edges.produce_more_card)
    graph.add_edge("format_card", END)

    return graph.compile()