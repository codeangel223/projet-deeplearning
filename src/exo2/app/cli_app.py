

from model.predict import predict_image
import os

CAT_FILENAME = "cat.9.jpg"
DOG_FILENAME = "dog.jpg"

TEST_FILE = CAT_FILENAME
# TEST_FILE = DOG_FILENAME


def run_cli_app():
    image_path = os.path.join(os.path.dirname(__file__), TEST_FILE)

    if not os.path.exists(image_path):
        print(f"❌ Fichier introuvable : {image_path}")
    else:
        label, prob = predict_image(image_path)
        print(f"✅ Résultat :  ({prob:.2f} {label})")
