

docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/03_battery_adjustment.md"

```
BATT_AMP_PERVLT = 147  # default = 55.9
BATT_AMP_OFFSET = 0.0275   # default = 0
```
