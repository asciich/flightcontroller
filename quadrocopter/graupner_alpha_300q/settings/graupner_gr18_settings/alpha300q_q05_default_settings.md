# Graupner Alpha 300q GR-18 default settings for Q5 Copter version

## Receiver settings

Should be equal to the [default settings Q4 copter version](alpha300q_q04_settings.md)
[Official release notes and download by Graupner](https://www.graupner.de/blog/detail/sCategory/737/blogArticle/179)

```
Receiver q.05 >
- Language:         english
- Ant1:     100%    Ant2: 100%
- Alarm Volt:       3.8 V
- max altitude      125m
- Period            20ms
- SUM at CH6:       No
- CH9:              SERVO

MULTICOPTER RO/NI < >
- ROLL/NICK P       22
- ROLL/NICH D       20
- DAMPING            2
- ROLLL FACTOR %    90
- POWER2SENS        80
- R/N DYNAMIC       50
- --ATTITUDE MODE--
- ROLL/NICK I       20
- AGILITY            5
- --RATE MODE--
R/N RATE I          20
RATE                30

MULTICOPTER YAW < >
- YAW P             52
- YAW I             25
- YAW D             11
- RAGE              50
- YAW DYNAMIC       80

MULTICOPTER BASE < >
- TYPE              QAUDRO X
- MODE              ACRO 3D
- ESC               ONESHOT
- MINPOWER %        8
- FREESTYLE         MIN
- CALIBR. POSITION  No
- LOGGING           1

GYRO ASSIGNMENT <
- do setup          No
- ROLL              -2
- NICK              -1
- YAW               -3
```

## Motor / ESC connections

[Full Alpha 300q Manual for more information](https://www.graupner.de/media/pdf/52/b6/bf/16530_3D_Copter_Alpha_300_DE5a31018fcc155.pdf)

```
        Front
  1 CW          2 CCW
      \        /
       \      /
        +----+
        |    |
        +----+
       /      \
      /        \
  4 CCW         3 CW
```