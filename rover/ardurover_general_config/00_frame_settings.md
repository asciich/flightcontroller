# Ardurover general frame settings

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/00_frame_settings.md"
```

# Default configuration assuming an rover (not a boat.)

```
FRAME_CLASS = 1   # 1 = Rover, see https://ardupilot.org/rover/docs/parameters.html#frame-class-frame-class
FRAME_TYPE = 0    # 0 = Undefined (which is default), see https://ardupilot.org/copter/docs/parameters.html#frame-type-frame-type-x-v-etc
```

Reboot your flightcontroller.
