# Log settings 

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/06_log_settings.md"
```

## Log backends

```
# LOG_BACKEND_TYPE = 0 # 0 = Logging disabled
LOG_BACKEND_TYPE = 1 # 1 = Logging only to file, not trough MavLink
```

## Always enable log:

```
LOG_DISARMED = 1 # 1 = Also log when disarmed, see https://ardupilot.org/rover/docs/parameters.html#log-disarmed-enable-logging-while-disarmed
```
