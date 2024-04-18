# Author: chthon@seas.upenn.edu

import re

import aiohttp
import cv2
import numpy as np
from fastapi import HTTPException, UploadFile
from qreader import QReader

qreader = QReader()


async def decode_qr_code(file: UploadFile):
    """
    Decode a QR code from the given file
    :param file: UploadFile
    :return: str
    """

    result = decode_qr_code_from_file(await file.read())

    if not result:
        # If no QR code is found, raise an HTTPException
        raise HTTPException(status_code=404, detail="No QR code found")

    return result


async def fetch_and_decode(url: str):
    """
    Fetch an image from the given URL and decode the QR code
    :param url: str
    :return: str
    """

    if not url:
        # If no URL is provided, raise an HTTPException
        raise HTTPException(status_code=400, detail="URL not provided")

    # Fetch the image from the URL asynchronously
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                # If the image cannot be fetched, raise an HTTPException
                raise HTTPException(status_code=400, detail="Unable to fetch image")

            # Read the image bytes and decode the QR code
            image_bytes = await response.read()
            return decode_qr_code_from_file(image_bytes)


def decode_qr_code_from_file(file: bytes):
    """
    Decode a QR code from the given file
    :param file: bytes
    :return: str
    """

    try:
        # Read the image from the file and convert it to RGB format
        image = cv2.cvtColor(
            cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_COLOR),
            cv2.COLOR_BGR2RGB,
        )

        # Detect and decode the QR code from the image
        result = qreader.detect_and_decode(image=image)

        if not result:
            # If no QR code is found, raise an HTTPException
            raise HTTPException(status_code=404, detail="No QR code found")

        return "\n".join(result)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


async def parse_wifi_credentials(file: UploadFile):
    """
    Parse Wi-Fi credentials from the given QR code
    :param file: UploadFile
    :return: dict
    """

    result = decode_qr_code_from_file(await file.read())

    # Regular expression pattern to match Wi-Fi credentials
    wifi_pattern = re.compile(r"^WIFI:T:(WPA|WEP|);S:(.+);P:(.+);;")

    match = wifi_pattern.search(result)
    if match:
        security = match.group(1)
        ssid = match.group(2)
        password = match.group(3)
        return {"SSID": ssid, "Password": password, "Security": security}
    else:
        return "QR code does not contain valid WiFi access information."
