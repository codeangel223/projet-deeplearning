import gradio as gr
from model.predict import predict_image
import os


def classify_image(image):
    """
    Fonction pour classifier une image de chien ou chat

    Args:
        image: Image uploadée par l'utilisateur

    Returns:
        tuple: (image, texte de prédiction)
    """
    if image is None:
        return None, "Aucune image fournie"

    temp_path = os.path.join(os.path.dirname(__file__), "temp.jpg")
    image.save(temp_path)

    label, prob = predict_image(temp_path)
    print("Prediction: ", label, prob)

    result_text = f"Prédiction: {label}\nConfiance: {prob:.2f}"

    try:
        os.remove(temp_path)
    except:
        pass

    return image, result_text


def run_gradio_app():
    """Lance l'application Gradio"""

    interface = gr.Interface(
        fn=classify_image,
        inputs=gr.Image(
            type="pil", label="Uploadez une image de chien ou chat"),
        outputs=[
            gr.Image(label="Image uploadée"),
            gr.Textbox(label="Résultat de la classification", lines=3)
        ],
        title="🐕 Chiens & Chat 🐱",
        description="Uploadez une image pour classifier si c'est un chien ou un chat",
        examples=None,
        theme=gr.themes.Soft()
    )

    # Lancer l'application
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )


def run_gradio_app_blocks():
    """Version avec Gradio Blocks pour plus de personnalisation"""

    with gr.Blocks(title="Chiens & Chat", theme=gr.themes.Soft()) as app:
        gr.Markdown("# 🐕 Chiens & Chat 🐱")
        gr.Markdown(
            "Uploadez une image pour classifier si c'est un chien ou un chat")

        with gr.Row():
            with gr.Column():
                input_image = gr.Image(
                    type="pil",
                    label="Image à classifier"
                )
                classify_btn = gr.Button("Classifier", variant="primary")

            with gr.Column():
                output_image = gr.Image(label="Image uploadée")
                result_text = gr.Textbox(
                    label="Résultat",
                    lines=3,
                    interactive=False
                )

        classify_btn.click(
            fn=classify_image,
            inputs=input_image,
            outputs=[output_image, result_text]
        )

        input_image.change(
            fn=classify_image,
            inputs=input_image,
            outputs=[output_image, result_text]
        )

    app.launch(
        server_name="0.0.0.0",
        server_port=7861,
        share=False
    )
