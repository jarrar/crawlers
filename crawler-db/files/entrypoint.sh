#!/bin/bash
set -o nounset
readonly SCRIPT=${0##*/}
export PYTHONDONTWRITEBYTECODE=1

function die() { echo $@; exit 1; }
function cleanup() { return 0;}

trap cleanup EXIT

uwsgi --ini /etc/uwsgi.ini

#python app.py

while true; do sleep 2; done
