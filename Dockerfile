FROM python:3.10-slim
WORKDIR /app
COPY backend/ /app
COPY frontend/ /app/frontend/
COPY backend/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
