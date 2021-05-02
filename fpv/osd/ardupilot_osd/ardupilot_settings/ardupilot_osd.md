# Ardupilot OSD

To upload these settings to a flightcontroller:

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/ardupilot_osd.md"
```

## General OSD settings

```
OSD_TYPE = 1        # 1 = MAX7456, see: https://ardupilot.org/rover/docs/parameters.html#osd-type-osd-type
OSD_UNITS = 0       # 0 = Metric
OSD_FONT = 2        # 2 = Betaflight bf-/ inav-ods default style
OSD_CELL_COUNT = 0  # 0 = autodetection for well charged LiPo
```

OSD offsets:

```
OSD_H_OFFSET = 32  # 32 = Default value
OSD_V_OFFSET = 16  # 16 = Default value
```

## OSD Warnings (blinking)

These settings should be overwritten by a model specific configuration.

```
OSD_W_RSSI = 30      # in %
OSD_W_NSAT = 9       # 9 = default settings
OSD_W_BATVOLT = 7.2  # 2S LiPo
```

## Enable/ Disable OSD Screesn

```
OSD1_ENABLE = 1  # 1 = Enabled
OSD2_ENABLE = 0  # 0 = Disabled
OSD3_ENABLE = 0  # 0 = Disabled
OSD4_ENABLE = 0  # 0 = Disabled
```

## Display elements

```
# Altitude over ground
OSD1_ALTITUDE_EN = 1
OSD1_ALTITUDE_X = 24
OSD1_ALTITUDE_Y = 10

# Main battery voltage
OSD1_BAT_VOLT_EN = 1
OSD1_BAT_VOLT_X = 11
OSD1_BAT_VOLT_Y = 12

# Main cell voltage
OSD1_AVGCELLV_EN = 1
OSD1_AVGCELLV_X = 16
OSD1_AVGCELLV_Y = 12

# Resting voltage
OSD1_RESTVOLT_EN = 0

# Other battery voltages
OSD1_BAT2_VLT_EN = 0
OSD1_BAT2USED_EN = 0
OSD1_CURRENT2_EN = 0

# RSSI
OSD1_RSSI_EN = 1
OSD1_RSSI_X = 1
OSD1_RSSI_Y = 2

# Main Battery current
OSD1_CURRENT_EN = 1
OSD1_CURRENT_X = 2
OSD1_CURRENT_Y = 12

# Main Battery used
OSD1_BATUSED_EN = 1
OSD1_BATUSED_X = 2
OSD1_BATUSED_Y = 14

# GPS number of acquired satellites
OSD1_SATS_EN = 1
OSD1_SATS_X = 0
OSD1_SATS_Y = 1

# Flightmode
OSD1_FLTMODE_EN = 1
OSD1_FLTMODE_X = 23
OSD1_FLTMODE_Y = 13

# Mavlink messages
OSD1_MESSAGE_EN = 1
OSD1_MESSAGE_X = 2  # default = 2
OSD1_MESSAGE_Y = 11   # default = 6

# GPS Ground speed
OSD1_GSPEED_EN = 1
OSD1_GSPEED_X = 1
OSD1_GSPEED_Y = 10

# Artificial horizon
OSD1_HORIZON_EN = 1  # default = 1
OSD1_HORIZON_X = 14  # default = 14
OSD1_HORIZON_Y = 8   # default = 8

# Distance and relative direction to home
OSD1_HOME_EN = 1
OSD1_HOME_X = 10
OSD1_Home_Y = 2

# Displays heading (in degrees)
OSD1_HEADING_EN = 0
OSD1_HEADING_X = 13  # default = 13
OSD1_HEADING_Y = 2   # default = 2

# Throttle sent to motors
OSD1_THROTTLE_EN = 1
OSD1_THROTTLE_X = 24
OSD1_THROTTLE_Y = 11

# Compass
OSD1_COMPASS_EN = 0
OSD1_COMPASS_X = 15  # default = 15
OSD1_COMPASS_Y = 3   # default = 3

# Wind speed
OSD1_WIND_EN = 0

# Airspeed used by TECS
OSD1_ASPEED_EN = 0

# Airspeed by primary airspeed sensor
OSD1_ASPD1_EN = 0

# Airspeed by secondary airspeed sensor
OSD1_ASPD2_EN = 0

# Climb rate / vertical speed
OSD1_VSPEED_EN = 1
OSD1_VSPEED_X = 25
OSD1_VSPEED_Y = 9

# ESC telemetry (BLHeli):
OSD1_BLHTEMP_EN = 0
OSD1_BLHRPM_EN = 0
OSD1_BLHAMPS_EN = 0

# GPS position latitude
OSD1_GPSLAT_EN = 1
OSD1_GPSLAT_X = 17
OSD1_GPSLAT_Y = 1

# GPS position longitude
OSD1_GPSLONG_EN = 1
OSD1_GPSLONG_X = 17
OSD1_GPSLONG_Y = 2

# Degrees from level
OSD1_ROLL_EN = 0
OSD1_PITCH_EN = 0

# Temperature by primary barometer
OSD1_TEMP_EN = 0

# Temperature by secondary barometer
OSD1_BTEMP_EN = 0

# Temperature by primary airspeed sensor
OSD1_ATEMP_EN = 0

# GPS HDOP
OSD1_HDOP_EN = 0

# Waypoint information
OSD1_WAYPOINT_EN = 0

# Crosstrack error
OSD1_XTRACK_EN = 0

# Total distance flown
OSD1_DIST_EN = 1
OSD1_DIST_X = 23
OSD1_DIST_Y = 3

# Flight stats
OSD1_STATS_EN = 0  # default = 0

# Total flight time
OSD1_FLTIME_EN = 1
OSD1_FLTIME_X = 22
OSD1_FLTIME_Y = 14

# Climb efficiency
OSD1_CLIMBEFF_EN = 0

# Flight efficiency
OSD1_EFF_EN = 0

# Clock panel (shows time)
OSD1_CLK_EN = 1
OSD1_CLK_X = 10
OSD1_CLK_Y = 1

# Things only on MSP (not MAX7456)
OSD1_SIDEBARS_EN = 0
OSD1_CRSSHAIR_EN = 0
OSD1_HOMEDIST_EN = 0
OSD1_HOMEDIR_EN = 0
OSD1_POWER_EN = 0
OSD1_CELLVOLT_EN = 0
OSD1_BATTBAR_EN = 0
OSD1_ARMING_EN = 0

# Callsign (Text from callsign.txt on SDCard root)
OSD1_CALLSIGN_EN = 1
OSD1_CALLSIGN_X = 10
OSD1_CALLSIGN_Y = 14

# VTX Power
OSD1_VTX_PWR_EN = 0

# Height above terrain
OSD1_TER_HGT_EN = 0
```


## Sources:

* OSD in rover documentation: https://ardupilot.org/rover/docs/common-osd-overview.html
