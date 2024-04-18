from pydantic import BaseModel


class UrlParser(BaseModel):
    url: str
