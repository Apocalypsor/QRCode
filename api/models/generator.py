# Author: chthon@seas.upenn.edu

from pydantic import BaseModel


class TextGenerator(BaseModel):
    """
    TextGenerator is a Pydantic model that represents the request body for generating a QR code with a given text.
    """

    text: str


class CustomGenerator(BaseModel):
    """
    CustomGenerator is a Pydantic model that represents the request body for generating a QR code with a given text,
    color, and logo.
    """

    text: str
    color: str = "black"
    # Logo is a base64 encoded image
    logo: str = None


class BatchGenerator(BaseModel):
    """
    BatchGenerator is a Pydantic model that represents the request body for batch generating QR codes with a list of
    texts.
    """

    texts: list[str] = []


class WifiGenerator(BaseModel):
    """
    WifiGenerator is a Pydantic model that represents the request body for generating a QR code with Wi-Fi credentials.
    """

    ssid: str
    password: str
    security_type: str
