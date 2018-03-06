FROM ubuntu:latest
MAINTAINER Jarrar Jaffari
ENV HTTPS_PROXY https://proxy-wsa.esl.cisco.com:80
ENV NO_PROXY locahost,127.0.0.0/8,.cisco.com,.tandberg.com,.huron-dev.com,.huron-alpha.com,.webex.com,.huron-int.com,.docker,172.27.12.196,172.27.12.195,172.27.12.197,172.27.12.191,172.27.12.207,10.30.123.70,10.30.123.71,10.30.123.72,10.30.122.80,10.30.122.81,10.30.122.82,10.30.122.83,10.30.122.84
ENV HTTP_PROXY http://proxy-wsa.esl.cisco.com:80
ENV https_proxy $HTTPS_PROXY
ENV http_proxy $HTTP_PROXY
ENV no_proxy $NO_PROXY


RUN apt-get update -y
RUN apt-get install -y build-essential \
                       vim             \
                       dnsmasq         \
                       python3-pip     \
                       python3-dev
RUN mkdir -p /app

ADD ./files/packages.txt /packages.txt

COPY ./app.py /app/app.py
COPY ./config.py /app/config.py
COPY ./__init__.py /app/
ADD ./models /app/models
ADD ./lib /app/lib

RUN pip3 install -r /packages.txt
COPY ./files/entrypoint.sh /app/entrypoint.sh
COPY ./files/uwsgi.ini /etc/uwsgi.ini

WORKDIR /app

ENTRYPOINT ["/app/entrypoint.sh"]
