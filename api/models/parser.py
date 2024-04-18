# Author: chthon@seas.upenn.edu

from pydantic import BaseModel


class UrlParser(BaseModel):
    """
    UrlParser is a Pydantic model that represents the request body for the /parse-qr-from-url endpoint.
    """

    url: str
