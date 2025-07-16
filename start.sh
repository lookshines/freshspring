#!/usr/bin/env bash
python manage.py migrate --noinput
gunicorn freshspring_website.wsgi:application