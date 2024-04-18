import os
import sys

import pytest
from fastapi.testclient import TestClient

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

client = TestClient(app)

current_dir = os.path.dirname(os.path.abspath(__file__))
qr_codes_dict = {
    "1.webp": "http://itunes.apple.com/us/app/encyclopaedia-britannica/id447919187?mt=8",
    "2.jpg": "http://searchmobilecomputing.techtarget.com/definition/2D-barcode",
}


@pytest.mark.asyncio
async def test_parse_qr():
    """
    Test parsing QR codes from images
    """

    for file_name, text in qr_codes_dict.items():
        with open(os.path.join(current_dir, "qr_code_images", file_name), "rb") as img:
            files = {"file": img}
            response = client.post("/parse-qr", files=files)
            assert response.status_code == 200
            assert response.text == text


@pytest.mark.asyncio
async def test_parse_qr_from_url():
    """
    Test parsing QR codes from URLs
    """

    data = {"url": "https://raw.githubusercontent.com/Apocalypsor/Trash/main/Courses/CIT5900/qrcodes/1.webp"}
    response = client.post("/parse-qr-from-url", json=data)
    assert response.status_code == 200
    assert response.text == "http://itunes.apple.com/us/app/encyclopaedia-britannica/id447919187?mt=8"


@pytest.mark.asyncio
async def test_batch_parse_qr_from_url():
    """
    Test parsing QR codes from multiple URLs
    """

    data = [
        {"url": "https://raw.githubusercontent.com/Apocalypsor/Trash/main/Courses/CIT5900/qrcodes/1.webp"},
        {"url": "https://raw.githubusercontent.com/Apocalypsor/Trash/main/Courses/CIT5900/qrcodes/2.jpg"},
    ]
    response = client.post("/batch-parse-qr-from-urls", json=data)
    assert response.status_code == 200
    assert response.json() == [
        "http://itunes.apple.com/us/app/encyclopaedia-britannica/id447919187?mt=8",
        "http://searchmobilecomputing.techtarget.com/definition/2D-barcode",
    ]


@pytest.mark.asyncio
async def test_parse_wifi_qr():
    """
    Test parsing WiFi QR codes
    """

    with open(os.path.join(current_dir, "qr_code_images", "wifi.png"), "rb") as img:
        files = {"file": img}
        response = client.post("/parse-wifi-qr", files=files)
        assert response.status_code == 200
        assert response.json() == {
            "SSID": "test",
            "Security": "WPA",
            "Password": "test",
        }
