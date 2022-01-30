

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/01_additional_settings_for_midnightgambler.md"
```

# Steering settings

```buildoutcfg
SERVO1_MIN = 1100
SERVO1_TRIM = 1500
SERVO1_MAX = 1900
```

# Throttle settings (onyl forward and higher range):
```
SERVO3_MIN = 1000 # Default 1100
SERVO3_MAX = 2000 # Defautl 1900
SERVO3_TRIM = 1000 # Default = 1500
MOT_SAFE_DISARM = 0 # Send PWM when disarmed
```