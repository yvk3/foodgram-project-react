FROM python:3.8.5

WORKDIR /app
RUN pip install gunicorn==20.1.0
COPY . .
RUN pip install -r requirements.txt && chmod +x /app/entrypoint.sh
ENTRYPOINT ["bash", "-c", "/app/entrypoint.sh"]

