import time

from AMavlinkDefaultObject import AMavlinkDefaultObject
from AMavlinkErrors import AMavlinkBootNotFinishedError


class AMavlinkSystem(AMavlinkDefaultObject):

    def __init__(self, amavlink):
        super(AMavlinkSystem, self).__init__()
        self._amavlink = amavlink

    def status(self):
        heartbeat_message = self._amavlink.heartbeat.wait()
        return heartbeat_message.system_status

    def uptime(self):
        system_time_message = self._amavlink.message.get_system_time(no_recv_buffer=True)
        return float(system_time_message.time_boot_ms) / 1000.0

    def wait_boot_finished(self):
        bootup_states = [
            self._enums['MAV_STATE_UNINIT'],
            self._enums['MAV_STATE_BOOT'],
            self._enums['MAV_STATE_CALIBRATING'],
        ]
        for i in range(60):
            if self.status() not in bootup_states:
                return
            time.sleep(1)
        raise AMavlinkBootNotFinishedError()

