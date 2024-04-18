from pydantic import BaseModel


class TextGenerator(BaseModel):
    text: str
