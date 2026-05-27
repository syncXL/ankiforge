# AnkiForge

AnkiForge is a CLI tool for turning PDF content into Anki flashcards. It extracts text from selected PDF pages, uses LLM prompts to estimate and generate cards, formats them as Anki note types, and pushes them into Anki through AnkiConnect.

## Features

- Generate cards from a PDF page range.
- Create or reuse an Anki deck/subdeck.
- Produce Basic, Basic reversed, and Cloze-style cards.
- Reuse existing Anki tags when formatting cards.
- Run the card generation workflow with LangGraph.

## Requirements

- Python 3.13+
- Anki desktop
- AnkiConnect add-on installed and running
- OpenRouter API key

## Setup

Install dependencies:

```powershell
uv sync
```

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
ANKI_URL=http://127.0.0.1:8765
```

Make sure Anki is open before generating cards so AnkiConnect can receive requests.

## Usage

Generate cards from a PDF:

```powershell
uv run ankiforge generate "path\to\file.pdf" --deck "My Deck"
```

Generate cards into a subdeck:

```powershell
uv run ankiforge generate "path\to\file.pdf" --deck "Medicine" --subdeck "Cardiology"
```

Limit generation to a page range:

```powershell
uv run ankiforge generate "path\to\file.pdf" --deck "Medicine" --start 3 --end 8
```

Options:

- `filepath`: path to the PDF file.
- `--deck`, `-d`: target Anki deck name.
- `--subdeck`, `-s`: optional subdeck name.
- `--start`: first page to process, using 1-based page numbers.
- `--end`: final page to process, using 1-based page numbers.

## Project Structure

```text
app/
  graphs/root/      LangGraph workflow, nodes, and routing
  models/           TypedDict and Pydantic models for cards and state
  services/         OpenRouter, retry, and AnkiConnect integrations
  main.py           Typer CLI entry point
prompts/            Prompt templates for estimation, generation, and formatting
```

## Notes

- Only PDF inputs are currently supported.
- Generated cards are added directly to Anki.
- The current LLM providers and model names are configured in `app/dependencies.py`.
