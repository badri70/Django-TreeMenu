#!/bin/bash
set -e

python manage.py migrate

python manage.py loaddata initial_menu.json || true

python manage.py runserver 0.0.0.0:8000
