FROM python:3.8.5-alpine3.12

RUN apk add wget
RUN wget -O eb.tar.gz https://github.com/blackducksoftware/exponential-backoff-tool/releases/download/0.0.4/eb_0.0.4_linux_amd64.tar.gz && tar -xvzf eb.tar.gz && mv /bin/eb /usr/bin

# Add dos2unix since we are working on windows and need to convert our files
RUN apk add dos2unix git

# Required for python cryptographic libraries
RUN apk add gcc musl-dev libffi-dev libressl-dev

# Required for Postgres
RUN apk add postgresql-libs postgresql-dev

# Add our source code
COPY source source

# Add Django web framework
RUN cd source && pip install -r requirements.txt

# Create empty directory to host our scripts
RUN mkdir -p /opt/scripts

# Everyone is running on windows, so we need to convert all our files to Unix prior to running
RUN find source/ -type f | xargs dos2unix

# By default, log in to the source directory
WORKDIR source

# Make our entrypoint executable
RUN chmod 755 entrypoint.sh

# By default, run our entrypoint.sh script
CMD ["./entrypoint.sh"]
