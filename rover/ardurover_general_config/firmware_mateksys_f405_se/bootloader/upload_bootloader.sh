#!/usr/bin/env bash

# Source: https://ardupilot.org/dev/docs/using-DFU-to-load-bootloader.html

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd "${SCRIPT_DIR}"

if dfu-util --list | grep "Found DFU:" ; then
  echo "Found devices to flash bootloader"
else
  echo "No DFU device found. Press the DFU button and then connect the Microcontroller to this computer."
  exit 1
fi

cd ${SCRIPT_DIR}
dfu-util -a 0 --dfuse-address 0x08000000 -D MatekF405-Wing_bl.bin

echo "upload bootloader finished."
