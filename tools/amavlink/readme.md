# AMavlink

Simple tool to communicate with vehicles using MAVLink.

* [Release Notes](release_notes.txt)

*IMPORTANT: Very early development state*
*IMPORTANT: Currently only available for Python2 since pymavlink does not support Python3*

## Installation

TODO

## Test AMavlink

All available tests are stored in the [tests](amavlink/tests/) directory. They can be executed using ```tox```

```bash
tox
```

The tests use the [asciich/ardupilot_sitl](https://github.com/asciich/docker-ardupilot_sitl) docker container to emulate a vehicle

## Additional information/ Sources

* [MAVLink common message set](http://mavlink.org/messages/common)
* [MAVLink commands on Ardupilot dev](http://ardupilot.org/dev/docs/mavlink-commands.html)
* Examples
** [Magteest example code](https://www.samba.org/tridge/UAV/pymavlink/unpacked/examples/magtest.py)