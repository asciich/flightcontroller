# HPI Racing Sprint2 Sport with Pixhawk flightcontroller.

This page describes the setup of my [HPI Racing Sprint2 Sport](http://www.hpiracing.com/en/kit/109299)
using a Pixhawk flightcontroller running [ArduRover firmware](../firmware/ardurover/).

[For blog posts and videos visit asciich.ch](https://asciich.ch/wordpress/category/hpi-racing-sprint2-sport-mustang/)

# Setup

## Hardware Setup

Connections:

* Pixhawk RC In <-> Frsky X8R SBus out.
* Pixhawk Telemetrie 2 -> Adapter Cable TODO -> SPort of Frsky X8R for Telemtry
* Pixhawk Main Out 1 -> Steering Servo
* Pixhawk Main Out 3 -> ESC

## Ardurover setup

### Flash firmware

Currently [version 3.5.2 of ArduRover](../firmware/ardurover/3.5.2) is used for the vehicle.

### Manual steps:

These steps were performed in [APMPlanner2](https://hub.docker.com/r/asciich/apmplanner2) manually.

1. Perform Compass calibration.
1. Perform Radio calibration.


### Automated steps:

To apply all these settings at once:
* (Start Mavproxy)[https://hub.docker.com/r/asciich/mavproxy]
* Upload these settings: For umploading all parameters at once [AMavlink]() can be used:
    ```
    docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/00_ardurover_setup.md"
    ```

1. Disable Failsafe
    ```
    FS_ACTION = 2 # Hold
    FS_THR_ENABLE = 0 # Do not use Throttle failsafe
    FS_GCS_ENABLE = 0 # Do not failsafe if connection to ground control station is lost.
    FS_EKF_ACTION = 1 # Hold
    FS_TIMEOUT = 1 # Failsafe after one second.
    ```

1. Set flight modes/ control modes [List of control modes](http://ardupilot.org/rover/docs/rover-control-modes.html)
    ```
    MODE_CH = 5 # Use RC channel 5 to set mode

    MODE1 = 0 # Manual
    MODE2 = 0 # Manual
    MODE3 = 1 # Acro
    MODE4 = 1 # Acro
    MODE5 = 10 # Auto
    MODE6 = 10 # Auto
    ```
1. Set ARM/Disarm switch and disable SafetySwitch
    ```
    RC7_OPTION = 41 # ARM/Disarm
    BRD_SAFETYENABLE = 0
    ```
1. Reverse steering servo
    ```
    SERVO1_REVERSED = 0
    ```
1. Frsky Telemetry on Telemetry2 port:
    ```
    SERIAL2_PROTOCOL = 10
    ```
1. [MinimOSD](https://github.com/night-ghost/minimosd-extra/wiki/APM) on Serial Port 4:
    ```
    SERIAL4_BAUD = 57  # telemetry output at 57600
    SERIAL4_PROTOCOL = 1 # MAVLink1
    ```
1. Serial connection to APSync TODO link on a RaspberryPi:
    # TODO px_uploader.py --port /dev/ttyACM0 /firmware/3.6.7/ArduCop  ter-v2.px4
    ```
    SERIAL5_PROTOCOL = 1 # MavLink version 1
    SERIAL5_BAUD = 921 # 921600 baud to communicate to the RaspberryPi
    ```
1. Compass Settings
    ```
    COMPASS_USE = 1
    COMPASS_USE2 = 0
    COMPASS_USE3 = 0
    COMPASS_LEARN = 0 # Disabled
    COMPASS_EXTERNAL = 0  # Only internal compass
    ```

## Sources:

* [Complete parameter list for ardurover](http://ardupilot.org/rover/docs/parameters.html)

