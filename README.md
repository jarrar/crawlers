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


