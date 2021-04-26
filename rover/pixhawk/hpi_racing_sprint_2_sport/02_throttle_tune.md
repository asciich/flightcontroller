# Throttle setup for HPI Racing Sprint2 Sport

To upload all settings in this file use:

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/02_throttle_tune.md"
```

## Settings

1. Maximum acceleration
    ```
    ATC_ACCEL_MAX = 2.0 # Default value = 2.0 m/s/s
    ```

1. ESC configuration
    ```
    MOT_PWM_TYPE = 0 # Normal PWM type
    MOT_SAFE_DISARM = 1 # No PWM output to motor when ArduRover is disarmed.
    ATC_BRAKE = 1 # Use brake functionality.
    MOT_THR_MIN = 5 # Min throttle percent.
    MOT_THR_MAX = 50 # Max throttle percent.

    SERVO3_MIN = 1100
    SERVO3_TRIM = 1500
    SERVO3_MAX = 1900

    MOT_SLEWRATE = 100 # Limit throttle changes to
    ```

1. Cruise Throttle and speed:
    *. To learn Cruise throttle enable function on a switch:
        ```
        # RC8_OPTION = 50 # learn cruise
        ```
    * Drive at the throttle speed and puth learn cruise throttle switch high for a few seconds. The parameters CRUISE_THROTTLE and CRUISE_SPEED are now updated and the new values are shown in the MavProxy command line output.
        ```
        CRUISE_THROTTLE = 31
        CRUISE_SPEED = 6.1
        ```

1. [Desired Speed to Throttle PID Tuning](http://ardupilot.org/rover/docs/rover-tuning-throttle-and-speed.html#desired-speed-to-throttle-pid-tuning)

    To see these values in APM Planner use GCS_PID_MASK=2

    ```
    ATC_SPEED_FF = 0.0 # Calculated from CRUISE_THROTTLE and CRUISE_SPEED so leave at 0.0
    ATC_SPEED_P = 0.2 # ; Original value: 0.2
    ATC_SPEED_I = 0.2 # ; Original value: 0.2
    ATC_SPEED_D = 0.0 # Normaly not used acording to the documentation.
    ```

## Sources:
    * [Tuning Speed and Throttle](http://ardupilot.org/rover/docs/rover-tuning-throttle-and-speed.html#desired-speed-to-throttle-pid-tuning)

