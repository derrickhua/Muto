from fastapi import UploadFile, File, HTTPException

async def upload_image(file: UploadFile = File(...)):
    try:
        file_name = file.filename
        return {"message": "Image uploaded successfully", "file_name": file_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


