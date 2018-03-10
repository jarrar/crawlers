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

# Docker image registry

Images are also stored in docker.io, the following are the images:
    * docker.io/jarrar/crawler-app
    * docker.io/jarrar/crawler-db
    * docker.io/jarrar/crawler-web

These are made public all you need is an account on docker.io.

# How to run in Development mode.

This application can be run in Develeopment or Production mode. By default if nothing specified
is Production. Use `orchestrated_app.sh` with `-d` option to indicate inetion to run it in the
Development mode.

In Development all code is used off of a workspace that is stored in env variable WORKSPACE
this whould be the dir where this repo was cloned, suppose that was a dir $HOME/mywork so
typically you would do:

```bash
cd $HOME/mywork
export WORKSPACE=$HOME/mywork
git clone git@github.com:jarrar/crawlers.git
cd crawlers
./tools/orchestrated_app.sh -d -r
```

# How to run it?
You can first build the required docker images, using command:

* `./tools/orchestrated_app.sh -r`

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
