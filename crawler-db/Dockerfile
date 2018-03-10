FROM ubuntu:latest
MAINTAINER Jarrar Jaffari

RUN apt-get update -y
RUN apt-get install -y build-essential \
                       vim             \
                       dnsmasq         \
                       python3-pip     \
                       python3-dev
RUN mkdir -p /app

ADD . /app/

#ADD ./files/ /app/files

COPY ./files/packages.txt /app/packages.txt


#COPY ./*.py /app/
#COPY ./app.py /app/app.py
#COPY ./config.py /app/config.py
#COPY ./__init__.py /app/

#ADD ./models /app/models
#ADD ./lib /app/lib

RUN pip3 install -r /app/packages.txt
COPY ./files/entrypoint.sh /entrypoint.sh
COPY ./files/uwsgi.ini /etc/uwsgi.ini

RUN apt-get install -y sqlite3

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
