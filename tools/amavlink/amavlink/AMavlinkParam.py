import time

from AMavlinkDefaultObject import AMavlinkDefaultObject
from AMavlinkErrors import AMavlinkParamVerificationError, AMavlinkParamNotReceiveError, AMavlinkParamSetError
from AMavlinkPramFile import AMavlinkParamFile


class AMavlinkParam(AMavlinkDefaultObject):

    def __init__(self, amavlink):
        super(AMavlinkParam, self).__init__()
        self._amavlink = amavlink

    def get(self, param_name):
        self._amavlink.heartbeat.wait_if_target_unknown()
        if isinstance(param_name, str):
            param_name = param_name.encode()
        mavutil = self._amavlink.get_mavutil()
        self._amavlink.message.clear_recv_buffer()
        for i in range(self.retries):
            mavutil.param_fetch_one(param_name)
            param_message = self._amavlink.message.get(type='PARAM_VALUE', blocking=True)
            if param_message is not None:
                break
            time.sleep(self.retry_delay)
        if param_message is None:
            raise AMavlinkParamNotReceiveError('param name: {}'.format(param_name))
        param_value = param_message.param_value
        return param_value

    def set(self, param_name, param_value):
        self._amavlink.heartbeat.wait_if_target_unknown()
        mavutil = self._amavlink.get_mavutil()
        if isinstance(param_name, str):
            param_name = param_name.encode()
        param_value = float(param_value)
        for i in range(self.retries):
            mavutil.mav.param_set_send(self._amavlink.heartbeat.system_id, self._amavlink.heartbeat.component_id,
                                       param_name, param_value, 0)
            read_value = self.get(param_name)
            if self.compare_values_equal(read_value, param_value):
                return
        raise AMavlinkParamSetError()

    def set_from_file(self, path):
        param_file = AMavlinkParamFile(path)
        param_file.read()
        for param_name in param_file:
            param_value = param_file[param_name]
            self.set(param_name, param_value)

    def verify_from_file(self, path):
        param_file = AMavlinkParamFile(path)
        param_file.read()
        for param_name in param_file:
            read_value = self.get(param_name)
            param_value = param_file[param_name]
            if not self.compare_values_equal(read_value, param_value):
                raise AMavlinkParamVerificationError('{} {} != {}'.format(param_name, param_value, read_value))
        return True

    def compare_values_equal(self, value, expected_value):
        if isinstance(value, float):
            return value == float(expected_value)
