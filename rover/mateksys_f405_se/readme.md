# Mateksys F405-SE arducrover firmware

* Ardupilot documentation for Mateksys F405-SE:
    * https://ardupilot.org/copter/docs/common-matekf405-se.html
* Mateksys F405-SE on Mateksys homepage:
    * http://www.mateksys.com/?portfolio=f405-se#tab-id-6


## Upload  bootloader:

use ```bootloader/upload_bootloader.sh```

## Upload firmware


```
docker run --rm --privileged -v $(pwd):/firmware -it asciich/px_uploader:latest /bin/bash
```

Upload firmware. Replace /dev/ttyACM0 and the firmware path to fit your need.

```
px_uploader.py --port /dev/ttyACM0 /firmware/arducopter_4_1_dev_20210212/arducopter.apj
```

