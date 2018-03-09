# crawlers
A web application that will accept a URL and store the number of characters (not bytes) in the HTTP
response message body.

# Setup required
* docker
* docker-compose
* Bash >= 3.x

# How to build it?
You can first build the required docker images, using command:

* `./tools/orchestrated_app.sh -b`

When you build it should build all the required docker images that you can
list:
`docker images`

# More Help

* `./tools/orchestrated_app.sh -h`

# Architecture

The application is made up of three micro services, namely:

1. crawler-app
   This is the micro service that opens port 5000 to the public and takes
   input from the user.

2. crawler-db
    This micro service provides REST based interface to all other micro services.

3. crawler-web
    This micro service interacts with the web and get responses off of the wwww and
    communicates through a REST interface.

# Design
