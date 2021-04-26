#!/usr/bin/env bash

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "${SCRIPT_DIR}"

if [ "$( ls /dev/ttyACM* | wc -l )" != "1" ] ; then
  echo "Unable to get port for flightcontroller."
  exit 1
fi

FC_PORT="$(ls /dev/ttyACM*)"
echo "Use FC_PORT='${FC_PORT}'"

docker run --rm --privileged -v ${SCRIPT_DIR}:/firmware -it asciich/px_uploader:latest /bin/sh -c \
  "px_uploader --port ${FC_PORT} /firmware/ardurover.apj"

