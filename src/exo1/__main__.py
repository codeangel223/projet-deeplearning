
# import os
from app.cli_app import run_cli_app
from app.streamlit_app import run_streamlit_app
from app.gradio_app import run_gradio_app


if __name__ == "__main__":
    # run_cli_app()  # Demarer le cli
    # run_streamlit_app()  # Demarer l'app streamlit
    run_gradio_app()  # Demarer l'app gradio

    # streamlit run src/exo1/__main__.py
