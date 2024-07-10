import streamlit as st
import cv2
import numpy as np
from PIL import Image
from utils import load_model, get_predictions, draw_boxes

#st.write("Upload an image of a parking lot to detect empty and occupied parking spaces.")



st.set_page_config(
    page_title="Parking space detection",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded")

# Custom CSS for sidebar and main page
st.markdown(
    """
    <style>
    /* Sidebar styles */
    [data-testid="stSidebar"] {
        background-color: black;
        color: white;
    }
    [data-testid="stSidebar"] .css-1l02zno {
        color: white;
    }

    /* Main page styles */
    .css-1d391kg {  /* Use this class to target the main page content area */
        background-color: gray;
    }
    .stApp {
        background-color: gray;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .white-text {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True)

st.sidebar.markdown('<h1 class="white-text">IMAGES AVAILABLE :</h1>', unsafe_allow_html=True)
st.markdown('<h1 class="white-text">PARKING SPACE DETECTION APP 🚗</h1>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
 



st.sidebar.image("img_test\img1.png", width=200, use_column_width=True)
st.sidebar.image("img_test\img2.png", width=200, use_column_width=True) 
st.sidebar.image("img_test\img3.png", width=200, use_column_width=True)
st.sidebar.image("img_test\img4.png", width=200, use_column_width=True) 

st.markdown('<h3 class="white-text">Please upload or select an image :</h3>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])


#uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])



if uploaded_file is not None:
    st.subheader("✔️ Uploaded Successfully ")
    image = Image.open(uploaded_file)
    image = np.array(image)

    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Detecting...")

    # Load the model
    model = load_model('Trained model/best.pt')

    # Get predictions
    results = get_predictions(model, image)

    # Draw bounding boxes
    result_image = draw_boxes(image, results)
    st.subheader("Detection Results:")
    # Display result image
    st.image(result_image, caption='Detected Image', use_column_width=True)

