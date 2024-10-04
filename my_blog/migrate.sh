#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"gahyun8876@gmail.com"}
cd /app/

/opt/virt/bin/python3 manage.py migrate --noinput
/opt/virt/bin/python3 manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true