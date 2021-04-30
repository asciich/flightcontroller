
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --upload /params/02_motor_settings.md"

## ESC configuration

Source:

```
MOT_PWM_TYPE = 0 # 0 = Normal
MOT_SAFE_DISARM = 1 # No PWM output to motor when ArduRover is disarmed.
```

## Remap motors:

Output CH1 is used for steering and CH3 for throttle:
* This is the default configuration for ArdoRover as documented in: https://ardupilot.org/rover/docs/rover-motor-and-servo-connections.html
* This allows us to use DShot for ESC and PWM for steering since the groups are separated on mateksys_f405_se: https://ardupilot.org/copter/docs/common-matekf405-se.html

```
SERVO1_FUNCTION = 26 # 26 = GroundSteering
SERVO2_FUNCTION = 0
SERVO3_FUNCTION = 70 # 70 = Throttle
SERVO4_FUNCTION = 0
```
