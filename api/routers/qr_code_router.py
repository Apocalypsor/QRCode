from io import BytesIO

from fastapi import APIRouter, Body, UploadFile
from fastapi.responses import StreamingResponse
from models.generator import TextGenerator
from models.parser import UrlParser
from services.qr_code_service import (
    decode_qr_code,
    fetch_and_decode,
    generate_qr_code,
)
from starlette.responses import PlainTextResponse

router = APIRouter()


@router.post("/parse-qr", response_class=PlainTextResponse)
async def parse_qr(file: UploadFile):
    return await decode_qr_code(file)


@router.post("/parse-qr-from-url", response_class=PlainTextResponse)
async def parse_qr_from_url(url_parser: UrlParser = Body(...)):
    return await fetch_and_decode(url_parser.url)


@router.post("/generate-qr")
async def generate_qr(text_generator: TextGenerator = Body(...)):
    qr_image = generate_qr_code(text_generator.text)
    img_byte_arr = BytesIO()
    qr_image.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    return StreamingResponse(img_byte_arr, media_type="image/png")
