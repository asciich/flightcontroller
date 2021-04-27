# Mateksys F405 SE settings for ardorover

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/01_mateksys_f405_se_settings.md"
```

Source: http://www.mateksys.com/?portfolio=f405-se#tab-id-6

```
BATT_VOLT_PIN = 10
BATT_VOLT_MULT = 11.0
BATT_CURR_PIN = 11
BATT_AMP_PERVLT = 55.9
```