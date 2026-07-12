import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(
    page_title="RoadGuard AI",
    page_icon="🚗",
    layout="wide"
)

# ---------------- Header ----------------

st.title("🚗 RoadGuard AI")
st.subheader("Real-Time Pothole Detection using Computer Vision")

st.markdown("---")

# ---------------- Sidebar ----------------

st.sidebar.title("RoadGuard AI")

st.sidebar.success("System Status : ACTIVE")

st.sidebar.markdown("""
### Features

✅ Real-Time Detection

✅ Voice Alert

✅ Screenshot Capture

✅ Detection Log

✅ Dashboard
""")

st.sidebar.markdown("---")

# ---------------- Detection Log ----------------

csv_path = "outputs/detections.csv"

if os.path.exists(csv_path):

    df = pd.read_csv(csv_path)

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Total Detections", len(df))

    with c2:
        st.metric("Project", "RoadGuard AI")

    st.markdown("---")

    st.subheader("📋 Detection History")

    st.dataframe(df, use_container_width=True)

else:

    st.warning("No detections found.")

# ---------------- Latest Screenshot ----------------

st.markdown("---")

st.subheader("📸 Latest Detection")

image_folder = "outputs"

images = []

if os.path.exists(image_folder):

    for file in os.listdir(image_folder):

        if file.endswith(".jpg"):

            images.append(file)

if len(images) > 0:

    latest = sorted(images)[-1]

    img = Image.open(os.path.join(image_folder, latest))

    st.image(img, width=700)

else:

    st.info("No screenshots available.")

# ---------------- Footer ----------------

st.markdown("---")

st.success("RoadGuard AI is Monitoring Roads Successfully 🚗")