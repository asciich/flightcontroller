import time

from pymavlink import mavutil

from AMAvlinkEeprom import AMavlinkEeprom
from AMavlinkCommand import AMavlinkCommand
from AMavlinkDefaultObject import AMavlinkDefaultObject
from AMavlinkFlightmode import AMavlinkFlightmode
from AMavlinkHeartbeat import AMavlinkHeartbeat
from AMavlinkLocation import AMavlinkLocation
from AMavlinkMessage import AMavlinkMessage
from AMavlinkParam import AMavlinkParam
from AMavlinkSystem import AMavlinkSystem


class AMavlink(AMavlinkDefaultObject):

    def __init__(self, port=None):
        super(AMavlink, self).__init__()
        mavutil.set_dialect('ardupilotmega')
        if port is None:
            self._port = 14551
        else:
            self._port = int(port)
        self._default_host = 'localhost'
        self._mavutil = None
        self._connect()
        self.command = AMavlinkCommand(self)
        self.eeprom = AMavlinkEeprom(self)
        self.flightmode = AMavlinkFlightmode(self)
        self.heartbeat = AMavlinkHeartbeat(self)
        self.location = AMavlinkLocation(self)
        self.message = AMavlinkMessage(self)
        self.param = AMavlinkParam(self)
        self.system = AMavlinkSystem(self)

    def close(self):
        self._mavutil.close()

    @property
    def connection_url(self):
        return 'udp:{}:{}'.format(self._default_host, self._port)

    def get_mavutil(self):
        return self._mavutil

    @property
    def is_connected(self):
        if self.heartbeat.wait(timeout=3) is None:
            return False
        else:
            return True

    @property
    def target_id(self):
        return self._mavutil.target_system

    def reconnect(self):
        self.close()
        time.sleep(1)
        self._connect()
        self.message.clear_recv_buffer()

    def _connect(self):
        self._mavutil = mavutil.mavlink_connection(self.connection_url, planner_format=False, notimestamps=True,
                                                   robust_parsing=True)
