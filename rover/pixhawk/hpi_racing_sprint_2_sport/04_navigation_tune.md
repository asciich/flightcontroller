# Stea setup for HPI Racing Sprint2 Sport

To upload all settings in this file use:

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/04_navigation_tune.md"
```

## Settings

1. Configure Speeds:
    ```
    RTL_SPEED = 4.5
    WP_SPEED = 4.5
    ```

1. Configure Turns:
    ```
    TURN_RADIUS = 0.89 # Default = 0.89
    TURN_MAX_G = 1.0 # Default = 0.6
    WP_RADIUS = 1.0 # Default = 2.0
    WP_OVERSHOOT = 1.0 # Default = 2.0
    ```

## Sources:
    * [Tuning navigation](http://ardupilot.org/rover/docs/rover-tuning-navigation.html)
