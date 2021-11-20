FROM python:3.9-alpine

# Create directory for the docker_bash_env user
RUN mkdir -p /home/app

# Create the docker_bash_env user
RUN addgroup -S app && adduser -S app -G app

# Add docker_bash_env

COPY app /app
WORKDIR /app

# chown all the files to the docker_bash_env user
USER root

RUN chown -R app:app /app

