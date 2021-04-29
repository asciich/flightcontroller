# Log settings 

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/06_log_settings.md"
```


```
LOG_BACKEND_TYPE = 1 # Logging only to file, not trough MavLink
```