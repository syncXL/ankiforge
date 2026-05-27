from typing import TypedDict, List, Annotated, Union, Literal
from pydantic import BaseModel, Field
from operator import add

class DeckState(TypedDict):
    content : str
    no_of_cards : int
    batch_size : int
    assessments : Annotated[list[str],add]
    tags : list[str]
    deck_name : str
    subdeck_name : str
    filepath : str
    start_page : int
    end_page : int

class Cards(BaseModel):
    assessments : List[str] = Field(description="The list of cards to generate")


class CardState(TypedDict):
    raw_card : str
    existing_tags : list[str]
    deck_name : str
    subdeck_name : str

class Basic(BaseModel):
    type: Literal["basic"] = "basic"
    front: str
    back: str
    reversed: bool
    tags: list[str]

class Cloze(BaseModel):
    type: Literal["cloze"] = "cloze"
    text: str
    tags: list[str]

class FormattedCard(BaseModel):
    card: Union[Basic, Cloze]