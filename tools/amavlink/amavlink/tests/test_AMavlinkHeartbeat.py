import pytest

from AMavlinkErrors import AMavlinkHeartbeatNotReceivedError


class TestAMavlinkHeartbeat(object):

    def test_wait(self, amavlink, arducopter_sitl):
        amavlink.system.wait_boot_finished()
        default_system_id = 1
        default_componet_id = 1
        amavlink.heartbeat.wait()
        assert default_system_id == amavlink.heartbeat.system_id
        assert default_componet_id == amavlink.heartbeat.component_id

    def test_heartbeat_system_state(self, amavlink, enums, arducopter_sitl):
        amavlink.system.wait_boot_finished()
        amavlink.system.status() == enums['MAV_STATE_STANDBY']

    @pytest.mark.skip('TODO implement')
    @pytest.mark.parametrize('timeout', [
        None,
        1,
        '1'
    ])
    def test_wait_heartbeat_raises_if_not_reachable(self, amavlink_noconnection, timeout):
        with pytest.raises(AMavlinkHeartbeatNotReceivedError):
            amavlink_noconnection.heartbeat.wait(timeout=timeout)

    @pytest.mark.skip('TODO implement')
    def test_send_heartbeat(self, amavlink):
        amavlink.send_heartbeat()
        amavlink.wait_heartbeat()
