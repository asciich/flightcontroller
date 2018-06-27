# AMavlink

Simple tool to communicate with vehicles using MAVLink.

* [Release Notes](release_notes.md)

**IMPORTANT: Very early development state**

**IMPORTANT: Currently only available for Python2 since pymavlink does not support Python3**

## Usage

Get single parameter (CH7_OPT):
```bash
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink param --get CH7_OPT"
```

Set single parameter (CH7_OPT to 8):
```bash
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink param --set CH7_OPT 8
```

Upload parameters from PARAM.FILE:

```bash
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/PARAM.FILE
```

Verify parameters from PARAM.FILE:

```bash
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --verify /params/PARAM.FILE
```

## Installation

It is recomended to use the [asciich/amavlink](https://hub.docker.com/r/asciich/amavlink/) docker container to run amavlink.
For local installation see [Installation with pip](installation_pip.md).

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