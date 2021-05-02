#!/usr/bin/env bash

# Sets up a virtualenv with MAVExplorer installed as described in:
# https://ardupilot.org/dev/docs/using-mavexplorer-for-log-analysis.html

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "${SCRIPT_DIR}"

virtualenv -p python3 ~/ve_mavexplorer
~/ve_mavexplorer/bin/pip install --upgrade pip
~/ve_mavexplorer/bin/pip install --upgrade \
  matplotlib \
  mavproxy \
  opencv-python \
  pymavlink \
  wxPython
