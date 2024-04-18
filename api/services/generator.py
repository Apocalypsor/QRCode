# Author: chthon@seas.upenn.edu

import base64
from io import BytesIO

import qrcode
from PIL import Image


def generate_qr_code(data):
    """
    Generate a QR code for the given data
    :param data: str
    :return: Image
    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)

    # Fit the QR code to the image size
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    return img


def generate_custom_qr_code(data, color="black", logo=None):
    """
    Generate a custom QR code with the given data, color, and logo
    :param data: str
    :param color: str
    :param logo: str, base64 encoded image
    :return: Image
    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)

    # Fit the QR code to the image size
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color=color, back_color="white")

    if logo:
        # logo is base64 encoded, decode it
        logo_data = base64.b64decode(logo)
        logo = Image.open(BytesIO(logo_data)).convert("RGBA")
        img = img.convert("RGBA")

        # Calculate dimensions to position the logo
        logo_size = img.size[0] // 3  # Logo size will be 1/3rd of the QR code size
        logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)

        # Calculate coordinates
        logo_pos = (
            (img.size[0] - logo.size[0]) // 2,
            (img.size[1] - logo.size[1]) // 2,
        )

        # Paste the logo on the QR code
        img.paste(logo, logo_pos, mask=logo)

    return img


def generate_wifi_qr(ssid, password, security_type):
    """
    Generate a QR code for the given Wi-Fi credentials
    :param ssid: str
    :param password: str
    :param security_type: str
    :return: Image
    """

    # Format: WIFI:T:<security>;S:<ssid>;P:<password>;;
    wifi_info = f"WIFI:T:{security_type};S:{ssid};P:{password};;"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_info)

    # Fit the QR code to the image size
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    return img
