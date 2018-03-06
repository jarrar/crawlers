#!/bin/bash
# Copyright (c) 1999 Cisco Systems, Inc.  All rights reserved.
# AUTHOR:  Jarrar Jaffari (), jjaffari@cisco.com
set -o nounset
readonly SCRIPT=${0##*/}
export PYTHONDONTWRITEBYTECODE=1

function die() { echo $@; exit 1; }
function cleanup() { return 0;}

trap cleanup EXIT

python app.py

while true; do sleep 2; done
