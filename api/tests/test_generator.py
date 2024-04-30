import os
import sys

import pytest
from fastapi.testclient import TestClient

from qr_code_images.logo_base64 import logo_base64

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_generate_qr():
    """
    Test geberate a QR Code
    """

    data = {"text": "Hello, World!"}
    response = client.post("/generate-qr", json=data)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"


@pytest.mark.asyncio
async def test_generate_custom_qr():
    """
    Test generate a custom QR Code
    """

    data = {
        "text": "Hello, World!",
        "color": "red",
        "logo": logo_base64,
    }
    response = client.post("/generate-custom-qr", json=data)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"


@pytest.mark.asyncio
async def test_generate_batch_qr():
    """
    Test generate multiple QR Codes
    """

    data = {"texts": ["Hello, World!", "Hello, QR Code!"]}
    response = client.post("/batch-generate-qr", json=data)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/zip"


@pytest.mark.asyncio
async def test_generate_wifi_qr():
    """
    Test generate WiFi QR Code
    """

    data = {
        "ssid": "test",
        "password": "password",
        "security_type": "WPA",
    }
    response = client.post("/generate-wifi-qr", json=data)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
