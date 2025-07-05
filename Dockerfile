FROM python:3.12.1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "src/exo1/__main__.py"]
# docker run build -t model-parasited-unfected .