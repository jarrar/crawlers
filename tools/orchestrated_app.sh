#!/bin/bash
# Copyright (c) 1999 Cisco Systems, Inc.  All rights reserved.
# AUTHOR:  Jarrar Jaffari (), jjaffari@cisco.com
set -o nounset
readonly SCRIPT=${0##*/}
readonly BASE_GIT_DIR=$(git rev-parse --show-toplevel)
readonly YAML_FILE=$BASE_GIT_DIR/orchestration/crawler.yml

readonly OPTIONS="hbr"
readonly OPTIONS_HELP=("Diplay this help text." \
                        "Builds the docker images for the entire project." \
                        "Runs the dockerized containers.")


function die() { echo $@; exit 1; }
function cleanup() { return 0;}

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
    which docker-compose &> /dev/null
    [[ $? -ne 0 ]] && die "$(hostname) is missing docker-compose please install it before running it."
}

function build_images()
{
    echo Building images
    docker-compose -f $YAML_FILE build

}

function main()
{
   [[ $BUILD_IMAGES == "yes" ]] && build_images
}

#
# execution loop starts from here
#

init

while getopts "$OPTIONS" opt; do
    case "$opt" in
        b) BUILD_IMAGES="yes" ; shift 1 ;;
        h) show_help          ; exit  0 ;;
        --) shift ; break ;;
        *) echo "Internal error!" ; exit 1 ;;
    esac
done

main