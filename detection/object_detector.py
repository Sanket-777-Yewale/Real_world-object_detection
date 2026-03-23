from ultralytics import YOLO
from config.settings import settings

class ObjectDetector:
    def __init__(self):
        self.model = YOLO(settings.MODEL_PATH)

    def detect(self, frame):
        results = self.model(frame)
        return results[0]