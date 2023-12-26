from fastapi import APIRouter, UploadFile, File
from app.controllers.image import image_controller

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return await image_controller.upload_image(file)
