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

    def __init__(self, port=None, debug_log_to_console=False):
        super(AMavlink, self).__init__()
        self._initialize_logger(debug_log_to_console)
        mavutil.set_dialect('ardupilotmega')
        if port is None:
            self._port = 14551
        else:
            self._port = int(port)
        self._default_host = '127.0.0.1'
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
        self.logger.info('AMavlink connection closed.')

    @property
    def connection_url(self):
        return 'udp:{}:{}'.format(self._default_host, self._port)

    def get_logger(self):
        return self.logger

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
        connection_url = self.connection_url
        self.logger.info('Connect to {}'.format(connection_url))
        self._mavutil = mavutil.mavlink_connection(connection_url, planner_format=False, notimestamps=True,
                                                   robust_parsing=True)

    def _initialize_logger(self, debug_log_to_console=False):
        """
        Source: https://docs.python.org/3/howto/logging-cookbook.html
        :return:
        """
        import logging

        logger = logging.getLogger('amavlink_logger')
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        log_hander = logging.FileHandler('amavlink.log')
        log_hander.setLevel(logging.INFO)
        log_hander.setFormatter(formatter)

        debug_log_handler = logging.FileHandler('amavlink_debug.log')
        debug_log_handler.setLevel(logging.DEBUG)
        debug_log_handler.setFormatter(formatter)

        if debug_log_to_console:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        logger.addHandler(log_hander)
        logger.addHandler(debug_log_handler)
        logger.info('AMavlink loggers initilaized')
        self.logger = logger
