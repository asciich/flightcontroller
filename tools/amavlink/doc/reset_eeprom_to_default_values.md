# AMavlink reset EEPROM to default values


**IMPORTANT: ALL SETTINGS ARE RESETED TO DEFAULT VALUES ON THE FLIGHTCONTROLLER**

```bash
docker run --net=host --rm -it asciich/amavlink sh -c "amavlink eeprom --reset-default-values"
```
