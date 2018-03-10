#!/bin/bash
# AUTHOR:  Jarrar Jaffari
set -o nounset
readonly SCRIPT=${0##*/}
readonly BASE_GIT_DIR=$(git rev-parse --show-toplevel)
readonly PROD_YAML_FILE=$BASE_GIT_DIR/orchestration/crawler/crawler.yml
readonly DEV_YAML_FILE=$BASE_GIT_DIR/orchestration/crawler/dev.yml
readonly TOOLS_DIR=$BASE_GIT_DIR/tools
readonly OAPP=$TOOLS_DIR/orchestrated_app.sh
readonly PARSE_YAML=$TOOLS_DIR/parse_yaml.py
readonly IMAGE_NAME_PATTERN="containers.cisco.com"
readonly DOCKER_USER_ID="jarrar"

readonly OPTIONS="hbrpd"
readonly OPTIONS_HELP=("Display this help text."            \
         "Builds the docker images for the entire project." \
         "Runs the dockerized containers."                  \
         "Publish docker images."                           \
         "Run in dev environment")

function die()     { echo $@  ; exit 1 ; }
function cleanup() { return 0 ; }
function green()    { echo -e "\e[32m$@\e[39m" ; }
function lt_green() { echo -e "\e[92m$@\e[39m" ; }
function red()      { echo -e "\e[31m$@\e[39m" ; }


trap cleanup EXIT

function show_help()
{
    local text=""
    echo ""
    echo $SCRIPT
    echo -e "\tThe script can be used to run orchestrated commands for this project."
    for (( i=0; i<${#OPTIONS}; i++ ))
    do
        echo -e "\t -${OPTIONS:$i:1}\t${OPTIONS_HELP[$i]}"
    done
    echo ""
}

function init()
{
    BUILD_IMAGES="no"
    PUBLISH_IMAGES="no"
    LAUNCH_CONTAINERS="no"
    DEVELOPMENT_ENV="no"
    YAML_FILE=$PROD_YAML_FILE

    which docker-compose &> /dev/null
    [[ $? -ne 0 ]] && die "$(hostname) is missing docker-compose please install it before running it."
    export COMPOSE_PROJECT_NAME=experiment
}

function build_images()
{
    echo Building images
    docker-compose -f $YAML_FILE build
}

function launch_containers()
{
    echo Stopping containers
    #docker-compose -f $YAML_FILE stop
    docker-compose -f $YAML_FILE down
    echo Launcching containers
    set -x
    docker-compose -f $YAML_FILE up -d
}
function show_env()
{
    cat <<-EOF
    YAML_FILE=$YAML_FILE
EOF
}

function publish_images()
{
  green Publishing following images:
  IMAGES=($(python $PARSE_YAML -f $DEV_YAML_FILE))

  lt_green ${IMAGES[*]}

  for img in ${IMAGES[@]}
  do
    green Publishing image:
    docker images | grep ^hcsg | grep $img
    id=$(docker images | grep ^experiment | grep $img | awk '{ print $3}')
    lt_green  - Tagging
    docker tag $id $DOCKER_USER_ID/${img}:latest
    docker push $DOCKER_USER_ID/${img}:latest
  done
}

function main()
{
   [[ $BUILD_IMAGES == "yes" ]]         && build_images
   [[ $LAUNCH_CONTAINERS == "yes" ]]    && launch_containers
   [[ $PUBLISH_IMAGES == "yes" ]]       && publish_images
}

#
# execution loop starts from here
#

init

while getopts "$OPTIONS" opt; do
    case "$opt" in
        b) BUILD_IMAGES="yes"       ;;
        p) PUBLISH_IMAGES="yes"     ;;
        r) LAUNCH_CONTAINERS="yes"  ;;
        d) YAML_FILE=$DEV_YAML_FILE ;;
        h) show_help                ; exit  0 ;;
        \?) echo "Internal error!" ; exit 1 ;;
    esac
done

show_env
main
