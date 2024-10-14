#!/bin/sh

echo "Entrypoint..."

cd /usr/src/app

# TODO: find a better way to wait for the db
echo "Waiting for the Database"
sleep 5

echo "Running Server..."
python manage.py runserver 0.0.0.0:8000