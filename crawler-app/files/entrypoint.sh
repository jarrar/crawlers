#!/bin/bash
set -o nounset
readonly SCRIPT=${0##*/}
export PYTHONDONTWRITEBYTECODE=1

function die() { echo $@ ; exit 1 ; }
function cleanup() { return 0 ;}
function launch_app() { uwsgi --ini /etc/uwsgi.ini ; }
function be_immortal() { while true; do sleep 2; done ; }

trap cleanup EXIT
#
# main loop
#
launch_app
be_immortal
