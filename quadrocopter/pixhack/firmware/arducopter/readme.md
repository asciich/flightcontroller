# Arducopter firmwares

## Programm PX4/ Pixhack/pixhack controller

Start docker container in this directory using:

```
docker run --rm --privileged -v $(pwd):/firmware -it asciich/px_uploader:latest /bin/bash
```

Upload firmware. Replace /dev/ttyACM0 and the firmware path to fit your need.

```
px_uploader.py --port /dev/ttyACM0 /firmware/3.6.12/ArduCopter-v2.px4
```

## Additional information/ Sources

* [Ardupilot Firmware](http://firmware.ardupilot.org/)
