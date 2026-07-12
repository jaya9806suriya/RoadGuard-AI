import pyttsx3
import time

engine = pyttsx3.init()
last_alert_time = 0

def speak():
    global last_alert_time

    current_time = time.time()

    # Speak only once every 5 seconds
    if current_time - last_alert_time > 5:
        engine.say("Warning! Pothole ahead.")
        engine.runAndWait()
        last_alert_time = current_time