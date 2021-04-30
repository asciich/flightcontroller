# Himoto Hummer 1/18 settings

To upload these settings use:
```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/01_himoto_hummer_1to18_settings.md"
```

## Steering servo settings

```
SERVO1_REVERSED = 1 # 1 = Reverse servo: https://ardupilot.org/rover/docs/parameters.html#servo1-reversed-servo-reverse
```

