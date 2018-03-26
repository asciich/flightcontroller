# APM2.8 connections for Acopter02

## Connect GR-12L Receiver

```
GR-12L Port 1 -> APM2.8 Port 3  # Throttle
GR-12L Port 2 -> APM2.8 Port 1  # Roll
GR-12L Port 3 -> APM2.8 Port 2  # Pitch
GR-12L Port 4 -> APM2.8 Port 4  # YAW
GR-12L Port 5 -> APM2.8 Port 5  # Flight mode
GR-12L Port 6 -> APM2.8 Port 7  # Special function
```

## Motor / ESC connections

```
        Front
  3 CW          1 CCW
      \        /
       \      /
        +----+
        |    |
        +----+
       /      \
      /        \
  2 CCW         4 CW
```

## Sources

* [Default APM channel map](http://ardupilot.org/copter/docs/common-rcmap.html)
* [Ardupilot connect ESCs and Motors](http://ardupilot.org/copter/docs/connect-escs-and-motors.html)