FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DOCKER_BUILDKIT=1
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["python", "nko_bot.py"]
#CMD ["uvicorn", "admin.main:app", "--host", "0.0.0.0", "--port", "8000"]
