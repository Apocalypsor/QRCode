from typing import List

from fastapi import APIRouter, Body, UploadFile
from starlette.responses import JSONResponse, PlainTextResponse

from models.parser import UrlParser
from services.parser import decode_qr_code, fetch_and_decode, parse_wifi_credentials

router = APIRouter()


@router.post("/parse-qr", response_class=PlainTextResponse)
async def parse_qr(file: UploadFile):
    return await decode_qr_code(file)


@router.post("/parse-qr-from-url", response_class=PlainTextResponse)
async def parse_qr_from_url(url_parser: UrlParser):
    return await fetch_and_decode(url_parser.url)


@router.post("/batch-parse-qr", response_class=JSONResponse)
async def batch_parse_qr(files: List[UploadFile] = Body(...)):
    results = []
    for file in files:
        result = await decode_qr_code(file)
        results.append(result)
    return JSONResponse(content=results)


@router.post("/batch-parse-qr-from-urls", response_class=JSONResponse)
async def batch_parse_qr_from_urls(url_parser: List[UrlParser] = Body(...)):
    results = []
    for url in url_parser:
        result = await fetch_and_decode(url.url)
        results.append(result)
    return JSONResponse(content=results)


@router.post("/parse-wifi-qr", response_class=JSONResponse)
async def parse_wifi_qr(file: UploadFile):
    wifi_details = await parse_wifi_credentials(file)
    return JSONResponse(content=wifi_details)
