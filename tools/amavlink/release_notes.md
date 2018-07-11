# AMavlink Release Notes

## v 0.07

* Parameters:
    * Added get_number_of_params.
    * Get parameters by index.
    * Get all parameters.
* Capture strmatch messages to stdout.

## v 0.06

* Increased floating point compare tollerance to 1e7.
* Fixed float compare in CLI to set parameters.

## v 0.05

* Travis CI support for Python2.7 added to automatically test amavlink implementation in pullrequests. Python 3 is still not supported.

## v 0.04

* Use relative error to compare float. This fixes the verification step for some values.

## v 0.03

* Added debug messages for param.set
* Fixed float compare to verify parameter values. 
* Use ```127.0.0.1``` instead of ```localhost``` for default connection.

## v 0.02

* Bugfix: Fixed get param instability.
* Added ```--debug``` flag to CLI.
* Clear EEPROM added to CLI.
* Support for markdown files as param.file.

## V 0.01

* CLI Support for parameters:
    * Set and get parameters from command line.
    * Set and verify parameters from file.