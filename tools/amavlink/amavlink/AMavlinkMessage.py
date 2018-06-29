import time

from AMavlinkDefaultObject import AMavlinkDefaultObject
from AMavlinkErrors import AMavlinkMessageNotReceivedError


class AMavlinkMessage(AMavlinkDefaultObject):

    def __init__(self, amavlink):
        super(AMavlinkMessage, self).__init__()
        self._amavlink = amavlink
        self._delay_between_reqeusts = 0.01

    def clear_recv_buffer(self):
        for i in range(1000):
            try:
                self.get()
            except AMavlinkMessageNotReceivedError:
                break

    def get(self, type=None, timeout=None, blocking=None):
        self._amavlink.heartbeat.wait_if_target_unknown()
        mavutil = self._amavlink.get_mavutil()
        if timeout is None:
            timeout = self.timeout
        self._amavlink.heartbeat.wait_if_target_unknown()
        if type is None:
            return self._recv_msg(timeout=timeout, blocking=blocking)
        elif type is not None:
            return mavutil.recv_match(type=type, blocking=blocking, timeout=timeout)

    def get_system_time(self, no_recv_buffer=False):
        if no_recv_buffer:
            self.clear_recv_buffer()
        return self._get_blocking_type(type='SYSTEM_TIME')

    def get_str_match(self, search_str, blocking=False, timeout=0):
        t_start = time.time()
        while True:
            try:
                message = self.get()
                if message is not None:
                    if search_str in str(message):
                        return message
                    else:
                        continue
            except AMavlinkMessageNotReceivedError:
                pass
            if not blocking:
                raise AMavlinkMessageNotReceivedError()
            else:
                self._sleep_if_timeout_not_expired(t_start, timeout)

    def _get_blocking_type(self, type):
        return self.get(type=type, timeout=self.timeout, blocking=True)

    def _sleep_if_timeout_not_expired(self, t_start, timeout):
        if timeout == 0:
            time.sleep(self._delay_between_reqeusts)
        elapsed_time = t_start - time.time()
        if elapsed_time >= timeout:
            raise AMavlinkMessageNotReceivedError()
        else:
            delay = min(timeout - elapsed_time, self._delay_between_reqeusts)
            time.sleep(delay)

    def _recv_msg(self, blocking=False, timeout=0):
        mavutil = self._amavlink.get_mavutil()
        t_start = time.time()
        while True:
            msg = mavutil.recv_msg()
            if msg is not None:
                return msg
            else:
                if not blocking:
                    raise AMavlinkMessageNotReceivedError()
                else:
                    self._sleep_if_timeout_not_expired(t_start, timeout)
