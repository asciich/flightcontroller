import pytest

from AMavlinkErrors import AMavlinkRCChannelInvalid


@pytest.mark.usefixtures("arducopter_sitl")
class TestAMavlinkRCInput(object):

    @pytest.mark.parametrize('channel, value', [
        (1, 1500),
        (2, 1500),
        (3, 1000),
        (4, 1500),
        (5, 1800),
        (6, 1000),
        (7, 1000),
        (8, 1800),
    ])
    def test_get_channel_pwm(self, amavlink, channel, value):
        amavlink.rcinput.deactivate_override()
        assert value == amavlink.rcinput.get_raw(channel)

    def test_deactiate_override(self, amavlink):
        channel = 6
        pwm_value = 2000

        amavlink.rcinput.deactivate_override()
        pwm_value_default = amavlink.rcinput.get_raw(channel=channel)

        amavlink.rcinput.override(channel=channel, pwm_value=pwm_value)
        assert pwm_value == amavlink.rcinput.get_raw(channel=channel)

        amavlink.rcinput.deactivate_override()
        assert pwm_value_default == amavlink.rcinput.get_raw(channel=channel)

    @pytest.mark.parametrize('channel,value', [
        (1, 1234),
        (1, 1111),
        (2, 1345),
        (3, 1355),
        (4, 1455),
        (5, 1239),
        (6, 1999),
        (7, 1765),
        (8, 1001),
    ])
    def test_overide_and_get_rc_input(self, amavlink, channel, value):
        """
        IMPORTANT: Overrides are automatically reset after 3 seconds.
        :param amavlink:
        :param channel:
        :param value:
        :return:
        """
        amavlink.rcinput.override(channel=channel, pwm_value=value)
        assert value == amavlink.rcinput.get_raw(channel=channel)

    @pytest.mark.parametrize('channel', [
        -1,
        0,
        9
    ])
    def test_override_with_invalid_channel_number(self, amavlink, channel, is_python3):
        if is_python3:
            expected_exception = AMavlinkRCChannelInvalid
        else:
            expected_exception = Exception
        with pytest.raises(expected_exception):
            amavlink.rcinput.override(channel=channel, pwm_value=1000)

    @pytest.mark.parametrize('channel', [
        -1,
        0,
        9
    ])
    def test_get_raw_with_invalid_channel_number(self, amavlink, channel, is_python3):
        if is_python3:
            expected_exception = AMavlinkRCChannelInvalid
        else:
            expected_exception = Exception
        with pytest.raises(expected_exception):
            amavlink.rcinput.get_raw(channel=channel)
