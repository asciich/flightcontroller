# Rover failsafe settings

```
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/10_failsafe.md"
```

## Ground station connection

```
FS_GCS_ENABLE = 0 # No action if connection lost to ground station
```

## Throttle failsafe

This is also triggered if signal gets lost on CRSF or SBUS

```
FS_THR_ENABLE = 0 # No throttle failsafe
FS_THR_VALUE = 910 # Minimal value = 910
```

## Battery failsafe

```
BATT_ARM_VOLT = 0
BATT2_ARM_VOLT = 0
BATT3_ARM_VOLT = 0
BATT4_ARM_VOLT = 0
BATT5_ARM_VOLT = 0
BATT6_ARM_VOLT = 0
BATT7_ARM_VOLT = 0
BATT8_ARM_VOLT = 0
BATT9_ARM_VOLT = 0

BATT_ARM_MAH = 0
BATT2_ARM_MAH = 0
BATT3_ARM_MAH = 0
BATT4_ARM_MAH = 0
BATT5_ARM_MAH = 0
BATT6_ARM_MAH = 0
BATT7_ARM_MAH = 0
BATT8_ARM_MAH = 0
BATT9_ARM_MAH = 0

BATT_LOW_VOLT = 0
BATT2_LOW_VOLT = 0
BATT3_LOW_VOLT = 0
BATT4_LOW_VOLT = 0
BATT5_LOW_VOLT = 0
BATT6_LOW_VOLT = 0
BATT7_LOW_VOLT = 0
BATT8_LOW_VOLT = 0
BATT9_LOW_VOLT = 0

BATT_CRT_VOLT = 0
BATT2_CRT_VOLT = 0
BATT3_CRT_VOLT = 0
BATT4_CRT_VOLT = 0
BATT5_CRT_VOLT = 0
BATT6_CRT_VOLT = 0
BATT7_CRT_VOLT = 0
BATT8_CRT_VOLT = 0
BATT9_CRT_VOLT = 0

BATT_LOW_MAH = 0
BATT2_LOW_MAH = 0
BATT3_LOW_MAH = 0
BATT4_LOW_MAH = 0
BATT5_LOW_MAH = 0
BATT6_LOW_MAH = 0
BATT7_LOW_MAH = 0
BATT8_LOW_MAH = 0
BATT9_LOW_MAH = 0

BATT_FS_LOW_ACT = 0 # No battery failsafe
BATT2_FS_LOW_ACT = 0 # No battery failsafe
BATT3_FS_LOW_ACT = 0 # No battery failsafe
BATT4_FS_LOW_ACT = 0 # No battery failsafe
BATT5_FS_LOW_ACT = 0 # No battery failsafe
BATT6_FS_LOW_ACT = 0 # No battery failsafe
BATT7_FS_LOW_ACT = 0 # No battery failsafe
BATT8_FS_LOW_ACT = 0 # No battery failsafe
BATT9_FS_LOW_ACT = 0 # No battery failsafe
```