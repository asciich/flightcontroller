import time

import pytest

pytest.mark.usefixtures("arducopter_sitl")


class TestAMavlinkTune(object):

    def test_enable_and_disable_tune_knop(self, amavlink):
        amavlink.tune.disable()
        assert float(0) == amavlink.param.get_value(param_name='TUNE')
        assert None == amavlink.tune.get_actual_tune_param_name()

        amavlink.tune.manual_tuning(amavlink.tune.RATEROLL_PITCH_KP)
        assert 4 == amavlink.param.get_value(param_name='TUNE')
        assert 'ATC_RAT_RLL_P' == amavlink.tune.get_actual_tune_param_name()

        amavlink.tune.disable()
        assert 0 == amavlink.param.get_value(param_name='TUNE')
        assert None == amavlink.tune.get_actual_tune_param_name()

    @pytest.mark.parametrize('default_value, tune_parameter, param_name, range_min, range_max, range_mid', [
        (0.1350, 'RATE_ROLL_PITCH_KP', 'ATC_RAT_RLL_P', None, None, None),
        (0.0900, 'RATE_ROLL_PITCH_KI', 'ATC_RAT_RLL_I', None, None, None),
        (0.0036, 'RATE_ROLL_PITCH_KD', 'ATC_RAT_RLL_D', 0.002, 0.004, 0.003),
    ])
    def test_tune_parameters(self, amavlink, default_value, tune_parameter, param_name, range_min, range_max,
                             range_mid):
        amavlink.tune.disable()
        amavlink.param.set(param_name, default_value)

        if range_min is None:
            range_min = default_value * 0.8
        if range_max is None:
            range_max = default_value * 1.2
        if range_mid is None:
            range_mid = default_value

        expected_tune_range = [
            range_min,
            range_max
        ]

        tune_values = [
            {'pwm_value': 1000, 'tune_value': range_min},
            {'pwm_value': 1500, 'tune_value': range_mid},
            {'pwm_value': 2000, 'tune_value': range_max},
        ]

        amavlink.tune.manual_tuning(tune_parameter)
        assert param_name == amavlink.tune.get_actual_tune_param_name()
        assert amavlink.param.compare_values_equal(default_value, amavlink.tune.get_original_value())
        self._assert_tune_range(amavlink, expected_tune_range)
        self._assert_tune_knop_values(amavlink, tune_values)

    def _assert_tune_range(self, amavlink, expected_tune_range):
        tune_range = amavlink.tune.get_tune_range()
        for i in range(len(expected_tune_range)):
            assert amavlink.param.compare_values_equal(expected_tune_range[i], tune_range[i])

    def _assert_tune_knop_values(self, amavlink, tune_values):
        for tune_value in tune_values:
            self._set_tune_knob_pwm(amavlink, pwm_value=tune_value['pwm_value'])
            assert tune_value['pwm_value'] == amavlink.tune.get_tune_knob_pwm()
            expected_tune_value = tune_value['tune_value']
            time.sleep(1)
            tune_value = amavlink.tune.get_actual_tune_value()
            assert amavlink.param.compare_values_equal(expected_tune_value, tune_value)

    def _set_tune_knob_pwm(self, amavlink, pwm_value):
        amavlink.rcinput.override(channel=6, pwm_value=pwm_value)
