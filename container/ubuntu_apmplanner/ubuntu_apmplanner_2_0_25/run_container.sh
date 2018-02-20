#!/usr/bin/env bash

set -e

xhost +SI:localuser:root

CONTAINER_NAME="ardupilot-$(pwgen 10 1)"

echo ""
echo "Start container"
VOLUMES="-v $(git rev-parse --show-toplevel):/git-repo/"
VOLUMES="${VOLUMES} -v /tmp/.X11-unix:/tmp/.X11-unix"
ENVIRONMENT="-e DISPLAY=${DISPLAY}"
CONTAINER=asciich/ubuntu_apmplanner:2.0.25
docker run --rm --privileged ${VOLUMES} ${ENVIRONMENT} --name ${CONTAINER_NAME} -it ${CONTAINER} /start_apmplanner2.sh

xhost +SI:localuser:root