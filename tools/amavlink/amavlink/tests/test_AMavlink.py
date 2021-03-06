import pytest


@pytest.mark.usefixtures("arducopter_sitl")
class TestAMavLink():

    def test_connection(self, amavlink):
        assert amavlink.is_connected

    def test_set_flight_mode_manual(self, amavlink):
        amavlink.flightmode.set_mode_manual()
        # TODO enable assert "MANUAL" == amavlink.flightmode.mode

    @pytest.mark.xfail(reason='TODO implement')
    def test_arm_disarm(self, amavlink):
        amavlink.command.arm()
        amavlink.command.disarm()
        # TODO enable: assert amavlink.arm_state == 'ARMED'
        # TODO enable: assert amavlink.disarm_state == 'DISARMED'

    def test_reconnect(self, amavlink):
        amavlink.heartbeat.wait()
        assert amavlink.target_id != 0
        amavlink.reconnect()
        assert amavlink.target_id == 0
