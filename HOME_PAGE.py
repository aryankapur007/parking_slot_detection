import streamlit as st


def centered_text(text, font_size=None, color=None):
    style = "text-align: center;"
    if font_size:
        style += f" font-size: {font_size};"
    if color:
        style += f" color: {color};"
    return f"<div style='{style}'>{text}</div>"

st.set_page_config(
    page_title="Home Page",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

#def run_appp():
#    subprocess.run(["python", "app.py", "appp"])


st.markdown(centered_text("<h1 style= 'color : red'>PARKING SLOT DETECTION APP 🚗</h1>"), unsafe_allow_html=True)
#st.divider()
st.markdown("<br>"
            "<br>", unsafe_allow_html=True)
st.markdown(centered_text("<h3>Welcome!</h3>"), unsafe_allow_html=True)
st.markdown(
    centered_text(
        "<p>This web application leverages a state-of-the-art YOLOv8 (You Only Look Once, version 8) model,<br>"
        " which has been meticulously trained on a custom dataset to detect cars in parking lots with high accuracy.</p>",
        color="darkgrey", font_size="16px"
        ),
        unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .sidebar-divider {
        background-color: red !important;
    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
#st.divider()
col1, col2, col3 = st.columns([10, 10, 10])


with col2:
    

    
    if st.button("DETECT NOW", key='Detect', help='Detect', type='primary', use_container_width=True):
        #subprocess.run(["streamlit", "run", "pages/DETECTION_SIMULATOR.py"])
        st.switch_page('pages/DETECTION_SIMULATOR.py')
        

#st.divider()

st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

#st.markdown("<br>", unsafe_allow_html=True)

st.markdown(centered_text("<h4>Why Use This App?</h4>", color="darkgrey"), unsafe_allow_html=True)
st.markdown(
        centered_text(
            "<p>"
            "Accurate Detection: Benefit from the latest advancements in object detection technology.<br>"
            "Time-Saving: Quickly identify available parking spaces without manually inspecting the entire lot.<br>"
            "Versatile: Useful for parking lot management, urban planning, and even personal use."
            "</p>",
            color="darkgrey"
        ),
        unsafe_allow_html=True
    )


