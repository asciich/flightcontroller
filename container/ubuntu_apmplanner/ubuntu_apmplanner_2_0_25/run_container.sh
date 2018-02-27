#!/usr/bin/env bash

set -e

CONTAINER_NAME="ardupilot-$(pwgen 10 1)"

echo ""
echo "Start container"
VOLUMES="-v $(git rev-parse --show-toplevel):/git-repo/"
VOLUMES="${VOLUMES} -v /tmp/.X11-unix:/tmp/.X11-unix"
VOLUMES="${VOLUMES} -v ${XAUTHORITY}:${XAUTHORITY}"
ENVIRONMENT="-e DISPLAY=${DISPLAY}"
ENVIRONMENT="${ENVIRONMENT} -e XAUTHORITY=${XAUTHORITY}"
CONTAINER=asciich/ubuntu_apmplanner:2.0.25

docker run --rm --net=host --privileged ${VOLUMES} ${ENVIRONMENT} --name ${CONTAINER_NAME} -it ${CONTAINER} /start_apmplanner2.sh
