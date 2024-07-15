import streamlit as st
import cv2
import sys
import numpy as np
from PIL import Image
import os

# Ensure the parent directory is in the sys.path
from utils import load_model, get_predictions, draw_boxes

def appp():

    

    st.set_page_config(
        page_title="Parking Space Detection",
        page_icon="🚗",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS for sidebar and main page
    st.markdown(
        """
        <style>
        
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
        unsafe_allow_html=True
    )

    #   Sidebar information
   # st.sidebar.markdown('<h1 class="white-text">MODEL INFORMATION :</h1>', unsafe_allow_html=True)
    #st.sidebar.markdown('<p class="white-text">This model detects empty parking spaces using a custom-trained YOLOv8 model, and uses streamlit to project the output.</p>', unsafe_allow_html=True)
    
# Custom CSS for highlighting text
    st.markdown(
    """
    <style>
    .highlight-text {
        color: white;
        background-color: red;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    </style>
    """
    , unsafe_allow_html=True
)

    st.sidebar.markdown('<h1 class="highlight-text">DETECTION SIMULATOR</h1>', unsafe_allow_html=True)
    st.markdown(
    """
    <style>
    .sidebar-divider {
        background-color: black !important;
    }
    </style>
    """
    , unsafe_allow_html=True
)

    st.sidebar.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown('<h2>SAMPLE IMAGES :</h2>', unsafe_allow_html=True)
    
    st.sidebar.image("img_test/img1.png", width=200, use_column_width=True)
    st.sidebar.image("img_test/img2.png", width=200, use_column_width=True)
    st.sidebar.image("img_test/img3.png", width=200, use_column_width=True)
    st.sidebar.image("img_test/img4.png", width=200, use_column_width=True)



    #st.markdown('<h1 class="white-text">PARKING SPACE DETECTION APP 🚗</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="white-text">PLEASE UPLOAD AN IMAGE :</h3>', unsafe_allow_html=True)
   
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([10, 5, 10])
    
    if uploaded_file is not None:
        with col1:
            st.subheader("✔️ Uploaded")
            image = Image.open(uploaded_file)
            image = np.array(image)

            st.image(image, caption='Uploaded Image', use_column_width=True)
        
        with col2:
            progress_bar = st.progress(0)

        try:
            # Load the model
            model = load_model('Trained model/best.pt')

            # Get predictions with progress update
            progress_bar.progress(50)
            results = get_predictions(model, image)

            # Draw bounding boxes
            result_image, count = draw_boxes(image, results)
            progress_bar.progress(100)
            with col3:
                st.subheader("Detection Results:")
                st.image(result_image, caption='Detected Image', use_column_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

            st.write("TOTAL PARKING SPACE AVAILABLE:",count)
            
            # Option to download the result image
            result_image_pil = Image.fromarray(result_image)
            result_image_pil.save('detected_image.png')
            with open('detected_image.png', 'rb') as file:
                st.download_button(
                    label="Download Detected Image",
                    data=file,
                    file_name="detected_image.png",
                    mime="image/png"
                )
            st.divider()
            st.write("How accurate was the detection?")
            choice = st.number_input("Rate accuracy between 0 to 5: ",min_value=0,  max_value=5 ,placeholder="Rate out of 10")
            if choice > 0:
                st.write(f"👍 Thank you for your feedback ! We will try to make it more accurate based on your answer.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

appp()
