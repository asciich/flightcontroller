# HPI racing sprint 2 sport throttle settings

To upload these settings use:
```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/02_hpi_racing_sprint_2_sport_throttle_settings.md"
```

## General throttle settings

```
MOT_SLEWRATE = 0  # 0 = No limitation, see: https://ardupilot.org/rover/docs/parameters.html#mot-slewrate-throttle-slew-rate
ATC_BRAKE = 1     # 1 = Use brake functionality
```
