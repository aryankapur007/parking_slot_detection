import streamlit as st
import cv2
import numpy as np
from PIL import Image
from utils import load_model, get_predictions, draw_boxes

st.title("Parking Lot Detection App")
st.write("Upload an image of a parking lot to detect empty and occupied parking spaces.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.array(image)

    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Detecting...")

    # Load the model
    model = load_model('best.pt')

    # Get predictions
    results = get_predictions(model, image)

    # Draw bounding boxes
    result_image = draw_boxes(image, results)

    # Display result image
    st.image(result_image, caption='Detected Image', use_column_width=True)
