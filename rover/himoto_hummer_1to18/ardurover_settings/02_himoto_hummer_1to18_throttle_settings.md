# Himoto Hummer 1/18 throttle settings

To upload these settings use:
```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/02_himoto_hummer_1to18_throttle_settings.md"
```

## General throttle settings

```
MOT_SLEWRATE = 0  # 0 = No limitation, see: https://ardupilot.org/rover/docs/parameters.html#mot-slewrate-throttle-slew-rate
ATC_BRAKE = 1     # 1 = Use brake functionality
```


