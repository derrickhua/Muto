from fastapi import UploadFile, File, HTTPException
import os
import shutil
from uuid import uuid4
from os import listdir
from os.path import isfile, join
from typing import List

async def upload_images(files: List[UploadFile]):
    responses = []

    # Get the absolute path of the controller file
    controller_dir = os.path.dirname(os.path.abspath(__file__))

    # Navigate two levels up from the controller file
    base_dir = os.path.dirname(os.path.dirname(controller_dir))

    # Construct the temp folder path
    temp_folder_path = os.path.join(base_dir, 'temp')

    # Ensure the temp directory exists
    os.makedirs(temp_folder_path, exist_ok=True)

    for file in files:
        try:
            # Generate a unique filename
            file_extension = os.path.splitext(file.filename)[1]
            temp_filename = f"{uuid4()}{file_extension}"

            # Temporary save location
            temp_path = os.path.join(temp_folder_path, temp_filename)

            with open(temp_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            responses.append({"message": "Image uploaded successfully", "file_name": temp_filename})
        except Exception as e:
            print(f"Error uploading file: {e}")  # Log any errors
            raise HTTPException(status_code=500, detail=str(e))

    return responses

    return responses

async def list_images():
    temp_folder_path = './temp'
    try:
        files = [f for f in listdir(temp_folder_path) if isfile(join(temp_folder_path, f))]
        return {"images": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def delete_images():
    temp_folder_path = '../../temp'
    for filename in os.listdir(temp_folder_path):
        file_path = os.path.join(temp_folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Images deleted successfully"}
