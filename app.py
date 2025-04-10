import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile
import os

# ==== CONFIG ==== #
MODEL_PATH = os.path.join("model", "best.pt")  # Path to your YOLOv8 model
model = YOLO(MODEL_PATH)

st.set_page_config(page_title="Glass/NoGlass Detection", layout="centered")

st.title("👓 Glass/NoGlass Detection")
st.write("Upload an image to detect glass or no-glass. Optionally convert it to greyscale before detection.")

# Upload image
uploaded_file = st.file_uploader("📤 Please upload an image", type=["jpg", "jpeg", "png"])

# Greyscale option
use_greyscale = st.checkbox("Convert image to greyscale before prediction")

if uploaded_file:
    # Convert to OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if use_greyscale:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Make it 3-channel again

    st.image(image, caption="📷 Original Image", use_column_width=True)

    # Save to temp file
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp_file:
        temp_path = tmp_file.name
        cv2.imwrite(temp_path, image)

    # Run YOLO model
    results = model(temp_path)

    for result in results:
        annotated = result.plot()

        # Show and allow download
        st.image(annotated, caption="✅ Annotated Image", use_column_width=True)

        # Encode to JPEG
        _, img_encoded = cv2.imencode(".jpg", annotated)

        st.download_button(
            label="📥 Download Annotated Image",
            data=img_encoded.tobytes(),
            file_name="annotated_image.jpg",
            mime="image/jpeg"
        )

    os.remove(temp_path)  # Cleanup
