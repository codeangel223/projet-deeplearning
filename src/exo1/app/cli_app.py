

from model.predict import predict_image
import os


def run_cli_app():
    image_path = os.path.join(os.path.dirname(__file__), "parasited.png")

    if not os.path.exists(image_path):
        print(f"❌ Fichier introuvable : {image_path}")
    else:
        label, prob = predict_image(image_path)
        print(f"✅ Résultat : {label} (probabilité : {prob:.2f})")
