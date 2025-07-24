import gradio as gr
from model.predict import predict_image
import os


def predict_and_display(image):
    """
    Fonction qui prend une image en entrée et retourne la prédiction
    """
    if image is None:
        return None, "Aucune image fournie"

    try:
        label, prob = predict_image(image)
        print("Prediction: ", label, prob)

        caption = f"{label} ({prob:.2f})"
        return image, caption

    except Exception as e:
        return image, f"Erreur lors de la prédiction: {str(e)}"


def run_gradio_app():
    """
    Lance l'application Gradio
    """

    interface = gr.Interface(
        fn=predict_and_display,
        inputs=gr.Image(
            type="filepath",
            label="Upload une image"
        ),
        outputs=[
            gr.Image(label="Image analysée"),
            gr.Textbox(label="Résultat de la prédiction")
        ],
        title="Détection de cellule infectée (Paludisme)",
        description="Uploadez une image pour détecter si les cellules sont infectées par le paludisme",
        examples=None
    )

    interface.launch(
        share=False,
        debug=True
    )


def predict_and_display(image):
    if image is None:
        return None, "Aucune image fournie"
    try:
        label, prob = predict_image(image, gradio_run=True)
        return image, f"{label} ({prob:.2f})"
    except Exception as e:
        return image, f"Erreur: {str(e)}"


def run_gradio_app():
    with gr.Blocks() as app:
        gr.Markdown("# Détection de cellule infectée (Paludisme)")
        gr.Markdown(
            "Uploadez une image pour analyser la présence de cellules infectées")

        with gr.Row():
            with gr.Column():
                input_image = gr.Image(
                    type="pil", label="Image à analyser")
                predict_btn = gr.Button("Analyser")
            with gr.Column():
                output_image = gr.Image(label="Résultat")
                prediction_text = gr.Textbox(label="Prédiction")

        predict_btn.click(predict_and_display, inputs=input_image, outputs=[
                          output_image, prediction_text])

    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )
