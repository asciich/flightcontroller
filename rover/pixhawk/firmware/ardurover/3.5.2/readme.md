# Ardurover 3.5.2 for Pixhawk PX4

## Flash ArduRover 3.5.2:

Start docker container to flash Ardurover in this directory:

```
docker run --rm --privileged -v $(pwd):/firmware -it asciich/px_uploader:latest /bin/bash
```

Use the following command to flash the firmware:

```
px_uploader.py --port /dev/ttyACM0 /firmware/ardurover.apj
```


*After flashing hold the SafetySwitch while booting to flash the internal IO-Board.*

# Sources/ Additional information

* Source: http://firmware.ardupilot.org/Rover/stable-3.5.2/Pixhawk1/