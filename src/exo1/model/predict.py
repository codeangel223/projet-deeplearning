import cv2
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


def predict_image(image_path):
    image = preprocess_image(image_path)
    prediction = model.predict(image)
    label = "Parasitized" if prediction[0][0] > 0.5 else "Uninfected"
    return label, prediction[0][0]
