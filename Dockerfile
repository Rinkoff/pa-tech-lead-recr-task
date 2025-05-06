FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

COPY . .

CMD ["streamlit", "run", "app.py"]