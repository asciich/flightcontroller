import pytest

@pytest.mark.usefixtures("arducopter_sitl")
class TestAMavlinkEeprom(object):

    def test_prepare_reset_to_default_parameters(self, amavlink):

        assert 0 != amavlink.param.get('SYSID_SW_MREV')
        amavlink.eeprom.prepare_reset_to_default_parameters()
        assert 0 == amavlink.param.get('SYSID_SW_MREV')