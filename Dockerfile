FROM python:3.8.5
ADD source source
ENTRYPOINT source/startup.sh