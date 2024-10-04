#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app/
/opt/virt/bin/gunicorn --worker-tmp-dir /dev/shm my_blog.wsgi:application --bind "0.0.0.0:${APP_PORT}"