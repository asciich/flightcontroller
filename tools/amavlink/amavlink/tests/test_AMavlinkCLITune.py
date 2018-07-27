import time
from threading import Thread

import pytest

from AMavlink import AMavlink
from HelperFunctions import assert_text_in_output


def emulate_channel6_knop():
    for pwm_value in [1000, 1500, 2000]:
        amavlink = AMavlink(port=14550)
        amavlink.rcinput.override(channel=6, pwm_value=pwm_value)
        time.sleep(5)


@pytest.mark.usefixtures("arducopter_sitl")
class TestAMavlinkCLITune(object):

    def test_disable_tune_parameters(self, amavlink_cli, amavlink, capsys):
        param_name = 'TUNE'
        param_value = 4
        tuning_disabled_value = 0

        amavlink.param.set(param_name=param_name, param_value=param_value)
        assert param_value == amavlink.param.get_value(param_name=param_name)

        amavlink_cli.main(['tune', '--disable'])
        assert tuning_disabled_value == amavlink.param.get_value(param_name=param_name)

        expected_text = ['Manual tuning disalbed']
        assert_text_in_output(capsys, expected_text)

    def test_tune_parameter_cli(self, amavlink_cli, amavlink, capsys):
        default_value = 0.1350
        param_name = 'ATC_RAT_RLL_P'

        amavlink.tune.disable()
        amavlink.param.set(param_name, default_value)
        assert amavlink.param.compare_values_equal(default_value, amavlink.param.get_value(param_name=param_name))

        cli_thread = Thread(target=emulate_channel6_knop)
        cli_thread.start()

        amavlink_cli.main(['tune', '--n_refresh', '20', '--rate-roll-pitch-kp'])

        cli_thread.join()

        expected_text = [
            'Start tuning RATE_ROLL_PITCH_KP',
            'Tune ATC_RAT_RLL_P; actual_value = 0.108000002801; tune_knob_pwm = 1000; original_value = 0.135000005364; range = [0.108, 0.162]',
            'Tune ATC_RAT_RLL_P; actual_value = 0.135000005364; tune_knob_pwm = 1500; original_value = 0.135000005364; range = [0.108, 0.162]',
            'Tune ATC_RAT_RLL_P; actual_value = 0.162000000477; tune_knob_pwm = 2000; original_value = 0.135000005364; range = [0.108, 0.162]',
        ]

        assert_text_in_output(capsys, expected_text)

    @pytest.mark.parametrize('cli_parameter, tune_param, param_name', [
        ('--rate-roll-pitch-kp', 'RATE_ROLL_PITCH_KP', 'ATC_RAT_RLL_P'),
        ('--rate-roll-pitch-ki', 'RATE_ROLL_PITCH_KI', 'ATC_RAT_RLL_I'),
        ('--rate-roll-pitch-kd', 'RATE_ROLL_PITCH_KD', 'ATC_RAT_RLL_D'),
    ])
    def test_tune_cli_parameters_are_correct(self, amavlink, amavlink_cli, capsys, cli_parameter, tune_param,
                                             param_name):
        amavlink.tune.disable()
        amavlink_cli.main(['tune', '--n_refresh', '2', cli_parameter])

        expected_text = [
            'Start tuning {}'.format(tune_param),
            'Tune {}'.format(param_name),
        ]

        assert_text_in_output(capsys, expected_text)
