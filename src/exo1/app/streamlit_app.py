

import streamlit as st
from model.predict import predict_image
import os


def run_streamlit_app():
    st.title("Détection de cellule infectée (Paludisme)")

    uploaded_file = st.file_uploader(
        "Upload une image ", type=["jpg", "png", "jpeg"]
    )

    if uploaded_file is not None:
        temp_path = os.path.join(os.path.dirname(__file__), "temp.jpg")
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())

        label, prob = predict_image(temp_path)
        print("Prediction: ", label, prob)
        st.image(
            temp_path,
            caption=f"{label}  ({prob:.2f})",
        )
