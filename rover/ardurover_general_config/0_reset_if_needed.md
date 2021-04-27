# Reset EEPROM

To reset the EEPROM run:
```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink param --set FORMAT_VERSION 0"
```

Then powercycle the flightcontroller.
