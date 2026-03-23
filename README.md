Gesture-Based Object Detection & Report Generation System

Overview

This project integrates gesture recognition, object detection, and report generation using YOLO and a modular Python architecture. Users can interact with the system via hand gestures to trigger real-time object detection and generate structured reports.

Key components:

Hand gesture recognition – Detects hand landmarks and counts fingers.
Object detection (YOLO) – Identifies objects in real-time video frames.
Report generation – Creates reports using detected objects and optional cloud-based analysis.

The system is implemented in a modular way to allow easy extension, testing, and integration of new detectors, gesture types, or reporting methods.

C:.
│   main.py                 # Entry point for the project
│   README.md
│   requirements.txt
│   vision-key.json         # API key for cloud vision services
│
├───camera                  # Handles camera input
│   └───camera_stream.py
│
├───cloud                   # Cloud API integration (optional)
│   └───vision_api.py
│
├───config                  # Configuration and logging
│   ├───logger.py
│   └───settings.py
│
├───database                # Database connections/models
│   ├───db_connection.py
│   └───models.py
│
├───detection               # YOLO object detection modules
│   ├───object_detector.py
│   ├───postprocess.py
│   └───roi_extractor.py
│
├───gesture                 # Gesture recognition and control
│   ├───hand_detector.py
│   ├───finger_counter.py
│   └───trigger_controller.py
│
├───llm                     # Report generation modules
│   └───report_generator.py
│
└───utils                   # Utility functions
    ├───bbox_utils.py
    └───image_utils.py

Project Flow

Camera Stream
CameraStream reads frames from the camera in real-time.
Hand Detection
HandDetector detects hand landmarks in each frame.
Finger Counting
FingerCounter counts the number of raised fingers.
Trigger Detection
TriggerController determines whether a gesture should trigger object detection and reporting.
Object Detection
ObjectDetector detects objects using YOLO on the current frame.
Report Generation
ReportGenerator compiles detected objects (and optional cloud labels) into structured reports.
Display & Loop
The processed frame is displayed with a live loop until the user exits (q key).

Installation
Clone the repository:
git clone <repository_url>
cd <project_folder>
Create and activate virtual environment:
python -m venv yolovenv
# Windows
yolovenv\Scripts\activate
# Linux/Mac
source yolovenv/bin/activate
Install dependencies:
pip install -r requirements.txt
Ensure the vision-key.json is set up for cloud vision API (optional).



How to Run

python main.py
The camera window will open showing real-time detection.
Use gestures (defined in TriggerController) to trigger object detection.
Reports will be printed in the console every 5 seconds when triggered.
Press q to quit.

Configuration

Report Interval: Controlled by REPORT_INTERVAL in main.py. Adjust to change frequency of report generation.
Camera Source: Modify CameraStream to switch between webcam or external cameras.
Cloud Vision API: Optional; configure in cloud/vision_api.py using vision-key.json.

| Module                     | Class             | Description                    |
| -------------------------- | ----------------- | ------------------------------ |
| camera.camera_stream       | CameraStream      | Captures video frames          |
| gesture.hand_detector      | HandDetector      | Detects hands in frames        |
| gesture.finger_counter     | FingerCounter     | Counts raised fingers          |
| gesture.trigger_controller | TriggerController | Determines trigger gestures    |
| detection.object_detector  | ObjectDetector    | Performs YOLO object detection |
| llm.report_generator       | ReportGenerator   | Generates structured reports   |
| cloud.vision_api           | VisionAPI         | Optional cloud label detection |








    
