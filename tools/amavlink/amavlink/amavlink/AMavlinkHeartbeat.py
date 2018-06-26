import time

from AMavlinkDefaultObject import AMavlinkDefaultObject
from AMavlinkErrors import AMavlinkHeartbeatNotReceivedError


class AMavlinkHeartbeat(AMavlinkDefaultObject):
    def __init__(self, amavlink):
        super(AMavlinkHeartbeat, self).__init__()
        self._amavlink = amavlink
        self._system_id = None
        self._component_id = None


    @property
    def component_id(self):
        if self._component_id is None:
            self.wait(timeout=self.timeout)
        return self._component_id

    @property
    def system_id(self):
        if self._system_id is None:
            self.wait(timeout=self.timeout)
        return self._system_id

    def wait_if_target_unknown(self):
        _ = self.component_id

    def send_heartbeat(self):
        '''
        Source https://discuss.bluerobotics.com/t/sending-mavproxy-messages-from-a-python-program/1515
        :return:
        '''
        mavutil = self._amavlink.get_mavutil()
        mavutil.mav.heartbeat_send(
            6,  # type
            8,  # autopilot
            192,  # base_mode
            0,  # custom_mode
            4,  # system_status
            3  # mavlink_version
        )

    def wait(self, timeout=None):
        mavutil = self._amavlink.get_mavutil()
        if timeout is None:
            timeout = self.timeout
        heart_beat = mavutil.recv_match(type='HEARTBEAT', blocking=True, timeout=timeout)
        if heart_beat is None:
            self._system_id = None
            self._component_id = None
            raise AMavlinkHeartbeatNotReceivedError()
        else:
            self._system_id = mavutil.target_system
            self._component_id = mavutil.target_component
        return heart_beat