import base64
from io import BytesIO

import qrcode
from PIL import Image


def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def generate_custom_qr_code(data, color="black", logo=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color="white")

    if logo:
        # logo is base64 encoded, decode it
        logo_data = base64.b64decode(logo)
        logo = Image.open(BytesIO(logo_data)).convert("RGBA")
        img = img.convert("RGBA")

        # Calculate dimensions to position the logo
        logo_size = img.size[0] // 3  # Logo size will be 1/3rd of the QR code size
        logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)

        # Calculate coordinates to place the logo
        logo_pos = (
            (img.size[0] - logo.size[0]) // 2,
            (img.size[1] - logo.size[1]) // 2,
        )
        img.paste(logo, logo_pos, mask=logo)

    return img


def generate_wifi_qr(ssid, password, security_type):
    # Format: WIFI:T:<security>;S:<ssid>;P:<password>;;
    wifi_info = f"WIFI:T:{security_type};S:{ssid};P:{password};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_info)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img
