# AMavlink

Simple tool to communicate with vehicles using MAVLink.

* [Release Notes](release_notes.md)

**IMPORTANT: Very early development state**

**IMPORTANT: Currently only available for Python2 since pymavlink does not support Python3**

## Connect to flightcontroller/ vehicle

AMavlink expects a with UDP-Port 14551 open on the same machine and **only one flightcontroller** connected.
[Mavproxy is also available as docker container for this purpose](https://hub.docker.com/r/asciich/mavproxy/)

## Usage

### EEPROM

* [Reset EEPROM to default values](docs/reset_eeprom_to_default_values.md)

### Single parameters

Get single parameter (CH7_OPT):
```bash
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink param --get CH7_OPT"
```

Set single parameter (CH7_OPT to 8):
```bash
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink param --set CH7_OPT 8
```

### Parameter files

Upload parameters from [PARAM.FILE](doc/param_file.md):

```bash
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/PARAM.FILE
```

Verify parameters from [PARAM.FILE](doc/param_file.md):

```bash
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --verify /params/PARAM.FILE
```

### Debug output

By adding ```--debug``` as command parameter the debug output is enabled.

## Installation

It is recomended to use the [asciich/amavlink](https://hub.docker.com/r/asciich/amavlink/) docker container to run amavlink.
For local installation see [Installation with pip](doc/installation_pip.md).

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
    * [Magtest example code](https://www.samba.org/tridge/UAV/pymavlink/unpacked/examples/magtest.py)