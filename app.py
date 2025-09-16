import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image

# =========================
# Page setup
# =========================
st.set_page_config(page_title="Skin Cancer Classifier", layout="centered")

# Change background color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;  /* Light blue, suitable for medical project */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# Load the model once
# =========================
@st.cache_resource
def load_my_model():
    model = load_model("myModel.keras")
    return model

model = load_my_model()

# =========================
# User Interface
# =========================
st.title("🩺 Skin Cancer Classification")
st.markdown("""
Upload a skin image and the model will predict whether it is benign or malignant.
""")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    st.subheader("Uploaded Image")
    st.image(uploaded_file, use_column_width=True)

    # Prepare the image for prediction
    img = Image.open(uploaded_file).convert("RGB")  # Convert any image to RGB
    input_shape = model.input_shape[1:3]           # Get model input size (height, width)
    img = img.resize(input_shape)                  # Resize to model input size

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize the image

    # Make prediction
    prediction = model.predict(img_array)

    # Display prediction result
    st.subheader("Prediction Result")
    if prediction.shape[-1] > 1:
        class_idx = np.argmax(prediction)
        st.write(f"Class: {class_idx} | Probabilities: {prediction}")
    else:
        st.write(f"Probability of positive class: {prediction[0][0]:.4f}")
