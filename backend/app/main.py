from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routers import image_router
import os

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows your frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include your routers
app.include_router(image_router.router)

# Get the directory of the current script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the temp folder
temp_folder_path = os.path.join(current_dir, 'temp')

app.mount("/temp", StaticFiles(directory=temp_folder_path), name="static")