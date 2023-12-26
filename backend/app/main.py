from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import image_router

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
