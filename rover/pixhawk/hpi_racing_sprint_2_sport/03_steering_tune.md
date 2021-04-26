# Steering setup for HPI Racing Sprint2 Sport

To upload all settings in this file use:

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/03_steering_tune.md"
```

## Settings

# To enable Gps Learn use:
# RC8_OPTION = 62

1. Set turn rate for ACRO mode:
    ```
    ACRO_TURN_RATE = 180 #  Default = 180.0
    ```

1. [Steering Rate PID Tuning](http://ardupilot.org/rover/docs/rover-tuning-steering-rate.html#steering-rate-pid-tuning):
    ```
    ATC_STR_RAT_FF = 0.2 # Default = 0.2
    ATC_STR_RAT_P = 0.2 # Can be left to 0 if ATC_STR_RAT_FF is well tuned; Default = 0.2
    ATC_STR_RAT_I = 0.2 # Default = 0.2
    ATC_STR_RAT_D = 0.0 # Normally not needed; Default = 0.0
    ```

## Sources:
    * [Tuning steering rate](http://ardupilot.org/rover/docs/rover-tuning-steering-rate.html)
