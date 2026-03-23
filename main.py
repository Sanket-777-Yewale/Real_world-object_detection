# import cv2
# import time   # ✅ NEW

# from camera.camera_stream import CameraStream
# from gesture.hand_detector import HandDetector
# from gesture.finger_counter import FingerCounter
# from gesture.trigger_controller import TriggerController
# from detection.object_detector import ObjectDetector
# from cloud.vision_api import VisionAPI
# from llm.report_generator import ReportGenerator

# cam = CameraStream()
# hand_detector = HandDetector()
# finger_counter = FingerCounter()
# trigger = TriggerController()
# detector = ObjectDetector()
# vision_api = VisionAPI()
# report_gen = ReportGenerator()

# # ✅ NEW: API rate control variables
# API_INTERVAL = 5   # seconds
# last_api_call_time = 0

# while True:
#     ret, frame = cam.read()
#     if not ret:
#         break

#     result = hand_detector.detect(frame)

#     if result.multi_hand_landmarks:
#         for hand_landmarks in result.multi_hand_landmarks:
#             count = finger_counter.count_fingers(hand_landmarks)
#             is_triggered = trigger.check_trigger(count)

#             if is_triggered:

#                 # Local YOLO detection (no restriction)
#                 yolo_result = detector.detect(frame)
#                 objects = [
#                     detector.model.names[int(cls)]
#                     for cls in yolo_result.boxes.cls
#                 ]

#                 # ✅ Time Check for Vision API
#                 current_time = time.time()

#                 if current_time - last_api_call_time >= API_INTERVAL:
#                     labels = vision_api.detect_labels(frame)
#                     last_api_call_time = current_time

#                     report = report_gen.generate(objects, labels)
#                     print("\n==== REPORT GENERATED ====")
#                     print(report)
#                 else:
#                     print("Waiting for 5 sec interval...")

#     cv2.imshow("Gesture System", frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cam.release()

#---------------------------------------------------------------------------------

import cv2
import time

from camera.camera_stream import CameraStream
from gesture.hand_detector import HandDetector
from gesture.finger_counter import FingerCounter
from gesture.trigger_controller import TriggerController
from detection.object_detector import ObjectDetector
from llm.report_generator import ReportGenerator

cam = CameraStream()
hand_detector = HandDetector()
finger_counter = FingerCounter()
trigger = TriggerController()
detector = ObjectDetector()
report_gen = ReportGenerator()

# Report interval control (avoid repeated generation)
REPORT_INTERVAL = 5   # seconds
last_report_time = 0

while True:
    ret, frame = cam.read()
    if not ret:
        break

    result = hand_detector.detect(frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            count = finger_counter.count_fingers(hand_landmarks)
            is_triggered = trigger.check_trigger(count)

            if is_triggered:

                # YOLO Detection
                yolo_result = detector.detect(frame)

                objects = [
                    detector.model.names[int(cls)]
                    for cls in yolo_result.boxes.cls
                ]

                # Use YOLO objects as labels
                labels = objects

                current_time = time.time()

                if current_time - last_report_time >= REPORT_INTERVAL:
                    last_report_time = current_time

                    report = report_gen.generate(objects, labels)

                    print("\n==== REPORT GENERATED ====")
                    print(report)
                else:
                    print("Waiting for 5 sec interval...")

    cv2.imshow("Gesture System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()