#!/bin/sh
cat motd.txt
echo "Starting Devops Task Server..."
# python3 ./helloworld.py
python3 manage.py runserver 0.0.0.0:8000
