from fastapi import APIRouter, UploadFile, File, HTTPException
from app.controllers.image import image_controller
from typing import List

router = APIRouter()
temp_folder_path = '../temp'

@router.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    try:
        responses = await image_controller.upload_images(files)
        return {"message": "Files processed successfully", "details": responses}
    except HTTPException as e:
        raise e


@router.get("/images")
async def get_images():
    try:
        return await image_controller.list_images()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete_images")
async def delete_images():
    try:
        return await image_controller.delete_images()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
