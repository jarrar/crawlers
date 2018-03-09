#!/bin/bash
set -o nounset
readonly SCRIPT=${0##*/}
export PYTHONDONTWRITEBYTECODE=1

function die() { echo $@; exit 1; }
function cleanup() { return 0;}

trap cleanup EXIT

#python microapp.py

uwsgi --ini /etc/uwsgi.ini



while true; do sleep 2; done
