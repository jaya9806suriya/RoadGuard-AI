from ultralytics import YOLO
import cv2
from alert import speak
from logger import log_detection
import os
import time

# Load trained model
model = YOLO("runs/detect/models/roadguard/weights/best.pt")

# Open video
cap = cv2.VideoCapture("videos/rod.mp4")

if not cap.isOpened():
    print("❌ Could not open the video.")
    exit()

print("✅ Video opened successfully.")

# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    # Detect potholes
    results = model(frame)

    # If pothole detected
    if len(results[0].boxes) > 0:

        speak()

        confidence = float(results[0].boxes.conf[0])

        log_detection(confidence)

        filename = f"outputs/pothole_{int(time.time())}.jpg"

        cv2.imwrite(filename, frame)

    # Draw detections
    annotated_frame = results[0].plot()

    # Project name
    cv2.putText(
        annotated_frame,
        "RoadGuard AI",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("RoadGuard AI", annotated_frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()