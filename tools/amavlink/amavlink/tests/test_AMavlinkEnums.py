import pytest


class TestAMavlinkEnums(object):

    def test_mav_state(self, enums):
        assert 0 == enums['MAV_STATE_UNINIT']
        assert 1 == enums['MAV_STATE_BOOT']
        assert 2 == enums['MAV_STATE_CALIBRATING']
        assert 3 == enums['MAV_STATE_STANDBY']
        assert 4 == enums['MAV_STATE_ACTIVE']
        assert 5 == enums['MAV_STATE_CRITICAL']
        assert 6 == enums['MAV_STATE_EMERGENCY']
        assert 7 == enums['MAV_STATE_POWEROFF']
        assert 8 == enums['MAV_STATE_ENUM_END']
