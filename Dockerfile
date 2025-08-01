FROM python:3.12.1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 7860
CMD ["python", "src/exo1/__main__.py"]
