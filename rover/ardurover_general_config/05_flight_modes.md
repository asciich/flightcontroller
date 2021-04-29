
To upload these settings use:

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/05_flight_modes.md"
```

```
MODE1 = 0 # Manual
MODE2 = 0 # Manual
MODE3 = 0 # Manual
MODE4 = 0 # Manual
MODE5 = 0 # Manual
MODE6 = 0 # Manual
```
