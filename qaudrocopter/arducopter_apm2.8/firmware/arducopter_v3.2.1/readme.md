# Flush APM2 controller with ArduCopter v3.2.1

Flush using asciich/ubuntu_avrdude container

1. Start ```asciich/ubuntu_avrdude``` container in current directory
```
docker run --rm --privileged -v $(pwd):/local_dir/ -it asciich/ubuntu_avrdude /bin/bash
```

2. Switch to local directory inside
```
cd /local_dir/
```

3. Flush controller:
```
avrdude -patmega2560 -cstk500v2 -P /dev/ttyACM0 -b115200 -D -Uflash:w:ArduCopter_v3.2.1.hex:i
```

4. Exit container
```
exit
```

[Source for this tutorial](http://firmware.ardupilot.org/)