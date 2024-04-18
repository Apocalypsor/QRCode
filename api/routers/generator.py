# Author: chthon@seas.upenn.edu

from io import BytesIO
from zipfile import ZipFile

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from models.generator import (
    BatchGenerator,
    CustomGenerator,
    TextGenerator,
    WifiGenerator,
)
from services.generator import (
    generate_custom_qr_code,
    generate_qr_code,
    generate_wifi_qr,
)

# Create a new FastAPI router
router = APIRouter()


@router.post("/generate-qr", response_class=StreamingResponse)
async def generate_qr(text_generator: TextGenerator):
    """
    Generate a QR code from the given text
    :param text_generator: TextGenerator
    :return: StreamingResponse
    """

    qr_image = generate_qr_code(text_generator.text)

    # Save the image to a byte array
    img_byte_arr = BytesIO()
    qr_image.save(img_byte_arr, format="PNG")

    # Reset the byte array's position to the beginning
    img_byte_arr.seek(0)

    return StreamingResponse(img_byte_arr, media_type="image/png")


@router.post("/generate-custom-qr", response_class=StreamingResponse)
async def generate_custom_qr(custom_generator: CustomGenerator):
    """
    Generate a custom QR code from the given text, color, and logo
    :param custom_generator: CustomGenerator
    :return: StreamingResponse
    """

    qr_image = generate_custom_qr_code(
        custom_generator.text, custom_generator.color, custom_generator.logo
    )

    # Save the image to a byte array
    img_byte_arr = BytesIO()
    qr_image.save(img_byte_arr, format="PNG")

    # Reset the byte array's position to the beginning
    img_byte_arr.seek(0)

    return StreamingResponse(img_byte_arr, media_type="image/png")


@router.post("/batch-generate-qr", response_class=StreamingResponse)
async def batch_generate_qr(batch_generator: BatchGenerator):
    """
    Generate a ZIP file containing QR codes for each text in the batch
    :param batch_generator: BatchGenerator
    :return: StreamingResponse
    """

    zip_byte_arr = BytesIO()
    with ZipFile(zip_byte_arr, "w") as zip_file:
        for text in batch_generator.texts:
            qr_image = generate_qr_code(text)

            # Save the image to a byte array
            img_byte_arr = BytesIO()
            qr_image.save(img_byte_arr, format="PNG")

            # Reset the byte array's position to the beginning
            img_byte_arr.seek(0)

            # Write the image to the ZIP file
            zip_file.writestr(f"{text}.png", img_byte_arr.getvalue())

    # Reset the ZIP file's position to the beginning
    zip_byte_arr.seek(0)

    return StreamingResponse(
        zip_byte_arr,
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=qr_codes.zip"},
    )


@router.post("/generate-wifi-qr", response_class=StreamingResponse)
async def generate_wifi_qr_endpoint(wifi_generator: WifiGenerator):
    """
    Generate a QR code for the given Wi-Fi credentials
    :param wifi_generator: WifiGenerator
    :return: StreamingResponse
    """

    qr_image = generate_wifi_qr(
        wifi_generator.ssid, wifi_generator.password, wifi_generator.security_type
    )

    # Save the image to a byte array
    img_byte_arr = BytesIO()
    qr_image.save(img_byte_arr, format="PNG")

    # Reset the byte array's position to the beginning
    img_byte_arr.seek(0)

    return StreamingResponse(img_byte_arr, media_type="image/png")
