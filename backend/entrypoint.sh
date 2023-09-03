#!/bin/sh

sleep 3
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn --bind 0:8000 backend.wsgi:application

exec "$@"