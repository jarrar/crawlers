FROM ubuntu:latest
MAINTAINER Jarrar Jaffari

RUN apt-get update  -y
RUN apt-get install -y python-pip python-dev build-essential

RUN mkdir -p /app

#ADD . /webapp
#RUN rm -f Dockerfile

COPY ./microapp.py /app/microapp.py
ADD ./files /app/files/.
COPY ./files/packages.txt /app/packages.txt
COPY ./files/uwsgi.ini /etc/uwsgi.ini

RUN pip install -r /app/files/packages.txt
COPY ./files/entrypoint.sh /entrypoint.sh

RUN apt-get install -y curl

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
