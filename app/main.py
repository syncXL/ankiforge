import asyncio
import typer
from pathlib import Path
from .graphs.root.graph import compile_graph_schema
from .dependencies import get_anki_loader

app = typer.Typer()

@app.command()
def generate(
    filepath: Path = typer.Argument(..., help="Path to PDF file"),
    deck: str = typer.Option(..., "--deck", "-d", help="Deck name"),
    subdeck: str = typer.Option("", "--subdeck", "-s", help="Subdeck name"),
    start: int = typer.Option(1, "--start", help="Start page"),
    end: int = typer.Option(None, "--end", help="End page"),
):
    asyncio.run(_run(filepath, deck, subdeck, start, end))


async def _run(filepath, deck, subdeck, start, end):
    ankiClient = get_anki_loader()
    existing_tags = await ankiClient.get_existing_tags()
    await ankiClient.ensure_deck(deck, subdeck)

    graph = compile_graph_schema()

    initial_state = {
        "filepath": str(filepath),
        "start_page": start-1,
        "end_page": end-1,
        "deck_name": deck,
        "subdeck_name": subdeck,
        "tags": existing_tags,
        "assessments": [],
        "no_of_cards": 0,
        "batch_size": 10,
    }

    result = await graph.ainvoke(initial_state)
    print(f"✅ Done. {len(result['assessments'])} cards pushed to Anki.")


def main():
    app()