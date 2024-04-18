from pydantic import BaseModel


class TextGenerator(BaseModel):
    text: str


class CustomGenerator(BaseModel):
    text: str
    color: str = "black"
    # Logo is a base64 encoded image
    logo: str = None


class BatchGenerator(BaseModel):
    texts: list[str] = []


class WifiGenerator(BaseModel):
    ssid: str
    password: str
    security_type: str
