import pytest


# TODO enalbe again @pytest.mark.usefixtures("arducopter_sitl")
import time


class TestAMavlinkTune(object):

    def test_enable_and_disable_tune_knop(self, amavlink):
        amavlink.tune.disable()
        assert float(0) == amavlink.param.get_value(param_name='TUNE')

        amavlink.tune.manual_tuning(amavlink.tune.RATEROLL_PITCHKP)
        assert 4 == amavlink.param.get_value(param_name='TUNE')

        amavlink.tune.disable()
        assert 0 == amavlink.param.get_value(param_name='TUNE')

    def test_tune_rate_roll_pitch_kp(self, amavlink):
        ATC_RAT_RLL_P_default_value = 0.135
        ATC_RAT_RLL_P_tune_min = ATC_RAT_RLL_P_default_value * 0.8
        ATC_RAT_RLL_P_tune_max = ATC_RAT_RLL_P_default_value * 1.2
        amavlink.param.set('ATC_RAT_RLL_P', ATC_RAT_RLL_P_default_value)

        amavlink.tune.manual_tuning(amavlink.tune.RATEROLL_PITCHKP)
        expected_tune_range = [
            ATC_RAT_RLL_P_tune_min,
            ATC_RAT_RLL_P_tune_max
        ]
        tune_range = amavlink.tune.get_tune_range()
        for i in range(len(expected_tune_range)):
            assert amavlink.param.compare_values_equal(expected_tune_range[i], tune_range[i])

        tune_values = {
            1000: ATC_RAT_RLL_P_tune_min,
            1500: ATC_RAT_RLL_P_default_value,
            2000: ATC_RAT_RLL_P_tune_max,
        }

        for pwm_value in tune_values:
            self._set_tune_knob_pwm(amavlink, pwm_value=pwm_value)
            expected_tune_value = tune_values[pwm_value]
            time.sleep(0.5)
            tune_value = amavlink.tune.get_actual_tune_value()
            assert amavlink.param.compare_values_equal(expected_tune_value, tune_value)


        # TODO repeat twice to make sure the high and low value do not depend on alredy tuned values


    def _set_tune_knob_pwm(self, amavlink, pwm_value):
        amavlink.rcinput.override(channel=6, pwm_value=pwm_value)
