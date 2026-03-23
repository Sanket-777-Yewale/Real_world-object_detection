import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    CAMERA_INDEX = 0
    GESTURE_REQUIRED_FINGERS = 5
    MODEL_PATH = "yolov8n.pt"

    GOOGLE_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

settings = Settings()