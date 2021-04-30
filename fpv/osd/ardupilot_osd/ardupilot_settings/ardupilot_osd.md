# Ardupilot OSD

To upload these settings to a flightcontroller:

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/ardupilot_osd.md"
```

## General OSD settings

```
OSD_TYPE = 1   # 1 = MAX7456, see: https://ardupilot.org/rover/docs/parameters.html#osd-type-osd-type
OSD_UNITS = 0  # 0 = Metric
OSD_FONT = 2   # 2 = Betaflight bf-/ inav-ods default style
```

OSD offsets:

```
OSD_H_OFFSET = 32  # 32 = Default value
OSD_V_OFFSET = 16  # 16 = Default value
```


## Sources:

* OSD in rover documentation: https://ardupilot.org/rover/docs/common-osd-overview.html
