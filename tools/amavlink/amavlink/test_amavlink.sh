#!/usr/bin/env bash

set -e

AMAVLINK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd ${AMAVLINK_DIR}
tox
