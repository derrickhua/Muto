from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_name = file.filename
        return {"message": "Files received", "file_name": file_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))