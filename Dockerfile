FROM python:3.8.5-alpine3.12

# Add dos2unix since we are working on windows and need to convert our files
RUN apk add dos2unix

# Add our source code
COPY source source

# Add Django web framework
RUN cd source && pip install -r requirements.txt

# Everyone is running on windows, so we need to convert all our files to Unix prior to running
RUN find source/ -type f | xargs dos2unix

# By default, log in to the source directory
WORKDIR source

# Make our entrypoint executable
RUN chmod 755 entrypoint.sh

# By default, run our entrypoint.sh script
CMD ["./entrypoint.sh"]
