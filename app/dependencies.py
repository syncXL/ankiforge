from pathlib import Path
from functools import lru_cache
from app.services.llm import LangchainOpenRouter
from app.services.anki import AsyncAnki
from app.config import settings

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

@lru_cache
def get_heavy_llm() -> LangchainOpenRouter:
    return LangchainOpenRouter(settings.openrouter_api_key, "google/gemma-4-26b-a4b-it")

@lru_cache
def get_max_llm() -> LangchainOpenRouter:
    return LangchainOpenRouter(settings.openrouter_api_key, "google/gemini-2.5-flash")

def read_text(file_path: str | Path, **params):
    resolved = PROMPTS_DIR / file_path if not Path(file_path).is_absolute() else Path(file_path)
    file = resolved.read_text(encoding="utf-8")
    if not params:
        return file
    return file.format(**params)


@lru_cache
def get_anki_loader() -> AsyncAnki:
    return AsyncAnki(url=settings.anki_url)