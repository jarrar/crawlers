FROM ubuntu:latest
MAINTAINER Jarrar Jaffari
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN mkdir -p /app
COPY ./app.py /app/app.py

COPY ./files/packages.txt /packages.txt
RUN pip install -r /packages.txt
COPY ./files/entrypoint.sh /app/entrypoint.sh

WORKDIR /app

ENTRYPOINT ["/app/entrypoint.sh"]
