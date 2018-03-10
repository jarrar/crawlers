FROM ubuntu:latest
MAINTAINER Jarrar Jaffari

RUN apt-get update -y
RUN apt-get install -y build-essential \
                       vim             \
                       dnsmasq         \
                       python3-pip     \
                       python3-dev
RUN mkdir -p /app
#ADD ./files /app/files

ADD . /app/

COPY ./files/packages.txt /app/packages.txt
#COPY ./*.py /app/

RUN pip3 install -r /app/packages.txt

COPY ./files/entrypoint.sh /entrypoint.sh
COPY ./files/uwsgi.ini /etc/uwsgi.ini

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
