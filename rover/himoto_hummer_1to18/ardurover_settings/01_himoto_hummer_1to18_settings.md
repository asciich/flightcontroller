# Himoto Hummer 1/18 settings

To upload these settings use:
```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/01_himoto_hummer_1to18_settings.md"
```

## Steering servo settings

```
SERVO1_REVERSED = 1 # 1 = Reverse servo: https://ardupilot.org/rover/docs/parameters.html#servo1-reversed-servo-reverse

SERVO1_TRIM = 1417  # default = 1500
SERVO1_MIN = 1017   # default = 1100
SERVO1_MAX = 1817   # default = 1100
```

## Battery settings

```
BATT_CAPACITY = 2200 # mAh
```
