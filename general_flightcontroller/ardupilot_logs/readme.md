# ArduPilot logs

Handling log files is described in this directory.

## Prepare SD-Card for ArduPilot which is also used for logging:

Format the SD-Card:
```
mkfs.fat -F32 /dev/sdcard
```

Add the callsign.txt file to the sdcard
```
echo "asciich" >> /mnt/sdcard/callsign.txt
```

Copy all font*.bin from fpv/osd/ardupilot_osd to the SD-card.

## Log analysis tools

### Offline analysis tools
* [MAVExplorer](mav_explorer)

### Browser based log analysis tools
* [https://plot.dron.ee/](https://plot.dron.ee/)
* [UAV Log Viewer](https://plot.ardupilot.org/#/) Browser based log file viewer.


