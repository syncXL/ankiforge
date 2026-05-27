import aiohttp
from ..models import root

class AsyncAnki:
    def __init__(self, url):
        self.url = url
    
    async def get_existing_tags(self) -> list[str]:
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json={"action": "getTags", "version": 6}) as response:
                result = await response.json()
                if result.get("error"):
                    print(f"❌ Failed to get tags: {result['error']}")
                    return []
                return result["result"]
    
    async def ensure_deck(self, deck_name: str, subdeck_name: str):
        full_deck = f"{deck_name}::{subdeck_name}"
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json={
                "action": "createDeck",
                "version": 6,
                "params": {"deck": full_deck}
            }) as response:
                result = await response.json()
                if result.get("error"):
                    print(f"❌ Failed to create deck: {result['error']}")
                    return False
                print(f"✅ Deck ready: {full_deck}")
                return True

    async def push_card(self, card: root.Basic | root.Cloze, deck_name: str, subdeck_name: str):
        full_deck = f"{deck_name}::{subdeck_name}"
        
        if isinstance(card, root.Basic):
            if not card.front.strip() or not card.back.strip():
                print("⚠️ Skipping empty Basic card")
                return None
            note = {
                "deckName": full_deck,
                "modelName": "Basic (and reversed card)" if card.reversed else "Basic",
                "fields": {"Front": card.front, "Back": card.back},
                "tags": card.tags
            }
        elif isinstance(card, root.Cloze):
            if not card.text.strip():
                print("⚠️ Skipping empty Cloze card")
                return None
            note = {
                "deckName": full_deck,
                "modelName": "Cloze",
                "fields": {"Text": card.text, "Back Extra": ""},
                "tags": card.tags
            }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json={
                "action": "addNote",
                "version": 6,
                "params": {"note": note}
            }) as response:
                result = await response.json()
                if result.get("error"):
                    print(f"❌ Failed to push card: {result['error']}")
                    return None
                print(f"✅ Card added with id: {result['result']}")
                return result["result"]

    async def store_urls(self):
        self.tags = await self.get_existing_tags()

