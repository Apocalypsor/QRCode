import re

import aiohttp
import cv2
import numpy as np
from fastapi import HTTPException, UploadFile
from qreader import QReader

qreader = QReader()


async def decode_qr_code(file: UploadFile):
    result = decode_qr_code_from_file(await file.read())
    if not result:
        raise HTTPException(status_code=404, detail="No QR code found")
    return result


async def fetch_and_decode(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="URL not provided")

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise HTTPException(status_code=400, detail="Unable to fetch image")
            image_bytes = await response.read()
            return decode_qr_code_from_file(image_bytes)


def decode_qr_code_from_file(file: bytes):
    try:
        image = cv2.cvtColor(
            cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_COLOR),
            cv2.COLOR_BGR2RGB,
        )
        result = qreader.detect_and_decode(image=image)
        if not result:
            raise HTTPException(status_code=404, detail="No QR code found")
        return "\n".join(result)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


async def parse_wifi_credentials(file: UploadFile):
    result = decode_qr_code_from_file(await file.read())
    wifi_pattern = re.compile(r"^WIFI:T:(WPA|WEP|);S:(.+);P:(.+);;")
    match = wifi_pattern.search(result)
    if match:
        security = match.group(1)
        ssid = match.group(2)
        password = match.group(3)
        return {"SSID": ssid, "Password": password, "Security": security}
    else:
        return "QR code does not contain valid WiFi access information."
