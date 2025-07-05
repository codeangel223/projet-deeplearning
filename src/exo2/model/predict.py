
from keras.utils import load_img, img_to_array
import numpy as np

import cv2
import os
import numpy as np
from keras.models import load_model

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model.h5")

model = load_model(model_path)


def process_image(img_path: str):
    img = load_img(img_path, target_size=(128, 128))

    img_array = img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)

    img_array /= 255.0

    return img_array


def predict_image(img_path: str):
    img_array = process_image(img_path)
    prediction = model.predict(img_array)[0][0]  # probabilité du chien

    label = "Dog" if prediction > 0.5 else "Cat"

    return label, float(prediction)
