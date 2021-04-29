# Ardurover general config

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/04_radio_calibration_and_configuration.md"
```

## Radio calibration

```
RC1_MIN = 987
RC1_TRIM = 1500
RC1_MAX = 2010

RC2_MIN = 987
RC2_TRIM = 1500
RC2_MAX = 2010

RC3_MIN = 987
RC3_TRIM = 1500
RC3_MAX = 2010

RC4_MIN = 987
RC4_TRIM = 1500
RC4_MAX = 2010

RC5_MIN = 987
RC5_TRIM = 1500
RC5_MAX = 2010

RC6_MIN = 987
RC6_TRIM = 1500
RC6_MAX = 2010

RC7_MIN = 987
RC7_TRIM = 1500
RC7_MAX = 2010

RC8_MIN = 987
RC8_TRIM = 1500
RC8_MAX = 2010

RC9_MIN = 987
RC9_TRIM = 1500
RC9_MAX = 2010

RC10_MIN = 987
RC10_TRIM = 1500
RC10_MAX = 2010

RC11_MIN = 987
RC11_TRIM = 1500
RC11_MAX = 2010

RC12_MIN = 987
RC12_TRIM = 1500
RC12_MAX = 2010

RC13_MIN = 987
RC13_TRIM = 1500
RC13_MAX = 2010

RC14_MIN = 987
RC14_TRIM = 1500
RC14_MAX = 2010

RC15_MIN = 987
RC15_TRIM = 1500
RC15_MAX = 2010

RC16_MIN = 987
RC16_TRIM = 1500
RC16_MAX = 2010
```

## Radio configuration

### CH1: Aileron

```
RCMAP_ROLL = 1
```

### CH2: Elevator

```
RCMAP_PITCH = 2
```

### CH3: Throttle

```
RCMAP_THROTTLE = 3
```

### CH4: Rudder

```
RCMAP_YAW = 4
```

### CH5: ARM

```
RC5_OPTION = 41 # 41 = Arm/Disarm
# Source: https://ardupilot.org/rover/docs/parameters.html#rc5-option-rc-input-option
```

### CH6: Motor Emergency Stop

```
RC6_OPTION = 31 # 31 = Motor Emergency stop
# Source: https://ardupilot.org/rover/docs/parameters.html#rc6-option-rc-input-option
```

### CH7: Drive mode (flight mode)

```
MODE_CH = 7 # https://ardupilot.org/rover/docs/parameters.html#mode-ch-mode-channel

RC7_OPTION = 0 # 0 = Do nothing
# Source: https://ardupilot.org/rover/docs/parameters.html#rc7-option-rc-input-option
```

### CH8: RTL

```
RC8_OPTION = 4 # 4 = RTL
# Source: https://ardupilot.org/rover/docs/parameters.html#rc8-option-rc-input-option
```
