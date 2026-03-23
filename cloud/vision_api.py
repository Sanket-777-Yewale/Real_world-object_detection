from google.cloud import vision
from google.oauth2 import service_account
import cv2

class VisionAPI:
    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(
            "vision-key.json"  
        )

        self.client = vision.ImageAnnotatorClient(credentials=credentials)

    def detect_labels(self, frame, min_confidence=0.75):
        success, buffer = cv2.imencode(".jpg", frame)
        if not success:
            return []

        image = vision.Image(content=buffer.tobytes())
        response = self.client.label_detection(image=image)

        if response.error.message:
            print("Vision API Error:", response.error.message)
            return []

        labels = [
            label.description
            for label in response.label_annotations
            if label.score >= min_confidence
        ]

        return labels