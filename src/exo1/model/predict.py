import cv2
from PIL import Image
import os
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model.h5")

model = load_model(model_path)


def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (50, 50))
    img = img_to_array(img)
    img = img.astype('float64') / 255.0
    img = np.expand_dims(img, axis=0)
    return img


def preprocess_image_gradio(image_input):
    if isinstance(image_input, str):
        img = cv2.imread(image_input)
    elif isinstance(image_input, np.ndarray):
        img = image_input
    elif isinstance(image_input, Image.Image):
        img = np.array(image_input)
    else:
        raise ValueError("Format d'image non supporté")

    if img is None:
        raise ValueError("Image non valide ou vide.")

    img = cv2.resize(img, (50, 50))
    img = img_to_array(img)
    img = img.astype('float64') / 255.0
    img = np.expand_dims(img, axis=0)
    return img


def predict_image(image_path, gradio_run: bool = False):
    image = None
    if gradio_run:
        image = preprocess_image_gradio(image_path)
    else:
        image = preprocess_image(image_path)
    prediction = model.predict(image)
    label = "Parasitized" if prediction[0][0] > 0.5 else "Uninfected"
    return label, prediction[0][0]
