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

router = APIRouter()


@router.post("/generate-qr", response_class=StreamingResponse)
async def generate_qr(text_generator: TextGenerator):
    qr_image = generate_qr_code(text_generator.text)
    img_byte_arr = BytesIO()
    qr_image.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    return StreamingResponse(img_byte_arr, media_type="image/png")


@router.post("/generate-custom-qr", response_class=StreamingResponse)
async def generate_custom_qr(custom_generator: CustomGenerator):
    qr_image = generate_custom_qr_code(
        custom_generator.text, custom_generator.color, custom_generator.logo
    )
    img_byte_arr = BytesIO()
    qr_image.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    return StreamingResponse(img_byte_arr, media_type="image/png")


@router.post("/batch-generate-qr", response_class=StreamingResponse)
async def batch_generate_qr(batch_generator: BatchGenerator):
    zip_byte_arr = BytesIO()
    with ZipFile(zip_byte_arr, "w") as zip_file:
        for text in batch_generator.texts:
            qr_image = generate_qr_code(text)
            img_byte_arr = BytesIO()
            qr_image.save(img_byte_arr, format="PNG")
            img_byte_arr.seek(0)
            zip_file.writestr(f"{text}.png", img_byte_arr.getvalue())

    zip_byte_arr.seek(0)
    return StreamingResponse(
        zip_byte_arr,
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=qr_codes.zip"},
    )


@router.post("/generate-wifi-qr", response_class=StreamingResponse)
async def generate_wifi_qr_endpoint(wifi_generator: WifiGenerator):
    qr_image = generate_wifi_qr(
        wifi_generator.ssid, wifi_generator.password, wifi_generator.security_type
    )
    img_byte_arr = BytesIO()
    qr_image.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    return StreamingResponse(img_byte_arr, media_type="image/png")
