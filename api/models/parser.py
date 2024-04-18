from fastapi import UploadFile
from pydantic import BaseModel


class FileParser(BaseModel):
    file: UploadFile


class UrlParser(BaseModel):
    url: str
