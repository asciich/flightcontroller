# HPI racing sprint 2 sport settings

To upload these settings use:
```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/01_hpi_racing_sprint_2_sport_settings.md"
```

## Steering servo settings

```
SERVO1_REVERSED = 0

SERVO1_TRIM = 1484  # default = 1500
SERVO1_MIN =  1084  # default = 1100
SERVO1_MAX =  1884  # default = 1900
```

## Battery settings

```
BATT_CAPACITY = 3000 # mAh
```
