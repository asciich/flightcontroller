import pytest


# TODO enalbe again @pytest.mark.usefixtures("arducopter_sitl")
class TestAMavlinkTune(object):

    def test_enable_and_disable_tune_knop(self, amavlink):
        amavlink.tune.disable()
        assert float(0) == amavlink.param.get_value(param_name='TUNE')

        amavlink.tune.manual_tuning(amavlink.tune.RATEROLL_PITCHKP)
        assert 4 == amavlink.param.get_value(param_name='TUNE')

        amavlink.tune.disable()
        assert 0 == amavlink.param.get_value(param_name='TUNE')

    @pytest.mark.xfail(reason='TODO implement')
    def test_tune_rate_roll_pitch_kp(self, amavlink):
        amavlink.tune.manual_tuning(amavlink.tune.RATEROLL_PITCHKP)
        # TODO assert tune hight
        # TODO assert tune low

        # TODO repeat twice to make sure the high and low value do not depend on alredy tuned values

        # RC_CHANNELS_RAW
        # RC_CHANNELS

# NEED TO PARSE THE RC CHANNEL AND RC_CHANNELS_RAW VALUES:

# Traceback (most recent call last):
#   File "/usr/bin/amavlink", line 11, in <module>
#     load_entry_point('amavlink==0.7', 'console_scripts', 'amavlink')()
#   File "/usr/lib/python2.7/site-packages/amavlink/AMavlinkCLI.py", line 168, in main
#     return amavlink_cli.main(sys.argv[1:])
#   File "/usr/lib/python2.7/site-packages/amavlink/AMavlinkCLI.py", line 54, in main
#     return self._run_param(args)
#   File "/usr/lib/python2.7/site-packages/amavlink/AMavlinkCLI.py", line 94, in _run_param
#     param_value = self._amavlink.param.get_value(param_name=param_name)
#   File "/usr/lib/python2.7/site-packages/amavlink/AMavlinkParam.py", line 47, in get_value
#     param_value = self.get(param_name=param_name).value
#   File "/usr/lib/python2.7/site-packages/amavlink/AMavlinkParameter.py", line 17, in value
#     self._value = self._param_message.param_value
# AttributeError: 'MAVLink_rc_channels_raw_message' object has no attribute 'param_value'
# / #
#
