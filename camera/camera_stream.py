import cv2
from config.settings import settings

class CameraStream:
    def __init__(self):
        self.cap = cv2.VideoCapture(settings.CAMERA_INDEX)

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()