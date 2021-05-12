# Serial configuration for ArduRover on Mateksys F405 SE

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/03_serial_configuration.md"
```


# Mapping:
See https://ardupilot.org/copter/docs/common-matekf405-se.html

SERIAL0 = console = USB
SERIAL1 = Telemetry1 = USART1
SERIAL2 = empty
SERIAL3 = GPS1 = USART3
SERIAL4 = GPS2 = UART4
SERIAL5 = USER = UART5
SERIAL6 = USER = USART6 (RX only; for ESC telemetry, use SERIAL6_PROTOCOL=16)
SERIAL7 = USER = USART2 (only if BRD_ALT_CONFIG =1)


# Serial configuration

## Disable RCINPUT default behaviour:
```
BRD_ALT_CONFIG = 1
```

## Mavlink Output on UART3 for TBS Tracer/ Crossfire CRSF

```
SERIAL3_PROTOCOL = 2 # Mavlink V2
SERIAL3_BAUD = 57
SERIAL3_OPTIONS = 0
```

## UART4 is not used

```
SERIAL4_PROTOCOL = -1 # -1 = Not used
SERIAL4_OPTIONS = 0
```

## GPS on UART5
```
SERIAL5_PROTOCOL = 5 # GPS
SERIAL5_BAUD = 38
SERIAL5_OPTIONS = 0
```

## USART6 is not used

```
SERIAL6_PROTOCOL = -1 # -1 = Not used
SERIAL6_OPTIONS = 0
```

# TBS Tracer/ Crossfire Protocol CRSF on UART7

```
SERIAL7_PROTOCOL = 23 # Automatically detect input.
RC_OPTIONS = 256 # Enable Crossfire passtrough
RSSI_TYPE=3
```

Reboot the fligthcontroller
