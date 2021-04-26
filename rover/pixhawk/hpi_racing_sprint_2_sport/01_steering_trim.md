# Trim setup for HPI Racing Sprint2 Sport

To upload all settings in this file use:

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/01_steering_trim.md"
```

## Settings

```
SERVO1_TRIM = 1540 # Readout from tarains X-Lite pro
```

## Sources:
    * [Save steering trim](http://ardupilot.org/rover/docs/savetrim.html)
    * [RC1_TRIM Parameter description](http://ardupilot.org/copter/docs/parameters.html#rc1-trim-rc-trim-pwm)
