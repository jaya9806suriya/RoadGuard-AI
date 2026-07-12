import csv
import os
from datetime import datetime

LOG_FILE = "outputs/detections.csv"

def log_detection(confidence):
    os.makedirs("outputs", exist_ok=True)

    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Time", "Confidence"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            round(confidence, 2)
        ])