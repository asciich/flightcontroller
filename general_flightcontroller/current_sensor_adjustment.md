# Current Sensor Adjustment

To adjust the current sensor:
* Read consumed mAh from OSD or log.
* Read charged mAH from charger.
* Calculate new scale:
    ```
    new_scale = old_scale * mah_consumed / mah_charged
    ```

Sources:
    * [How to Calibrate Current Sensor by Oscar Liang](https://oscarliang.com/current-sensor-calibration/)
