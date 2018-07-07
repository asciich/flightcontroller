import time

import math

from AMavlinkDefaultObject import AMavlinkDefaultObject
from AMavlinkErrors import AMavlinkParamVerificationError, AMavlinkParamNotReceiveError, AMavlinkParamSetError, \
    AMavlinkMessageNotReceivedError
from AMavlinkPramFile import AMavlinkParamFile


class AMavlinkParam(AMavlinkDefaultObject):

    def __init__(self, amavlink):
        super(AMavlinkParam, self).__init__(amavlink)
        self._amavlink = amavlink

    def get(self, param_name):
        self._amavlink.heartbeat.wait_if_target_unknown()
        if isinstance(param_name, str):
            param_name = param_name.encode()
        self.logger.info('Get param "{}" requested'.format(param_name))

        param_value = self._get_param_value(param_name)
        self.logger.info('Get param "{}" == {}'.format(param_name, param_value))
        return param_value

    def set(self, param_name, param_value):
        self._amavlink.heartbeat.wait_if_target_unknown()
        mavutil = self._amavlink.get_mavutil()
        if isinstance(param_name, str):
            param_name = param_name.encode()
        param_value = float(param_value)
        for i in range(self.retries):
            self.logger.info('Set param "{}" to "{}"'.format(param_name, param_value))
            mavutil.mav.param_set_send(self._amavlink.heartbeat.system_id, self._amavlink.heartbeat.component_id,
                                       param_name, param_value, 0)
            self.logger.debug('Readback param "{}" to verify param.set was successful'.format(param_name))
            read_value = self.get(param_name)
            if self.compare_values_equal(read_value, param_value):
                return
            else:
                self.logger.warning(
                    'param.set: Readback param "{}" failed: expected "{}" != "{}" readback'.format(param_name,
                                                                                                   param_value,
                                                                                                   read_value))

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
            return self._float_compare(value, expected_value)
        elif isinstance(value, str):
            return self._float_compare(value, expected_value)
        elif isinstance(value, int):
            return value == int(float(expected_value))
        else:
            raise Exception('Unknown type for comparison')

    def _float_compare(self, val1, val2, allow_relative_error=4e-8):
        if float(val1) == float(val2):
            return True
        if float(val2) == 0.0:
            val_tmp = val2
            val2 = val1
            val1 = val_tmp
        relative_error = abs(float(val1) - float(val2)) / abs(float(val2))
        if relative_error <= allow_relative_error:
            return True
        else:
            return False

    def _get_param_value(self, param_name):
        mavutil = self._amavlink.get_mavutil()
        self._amavlink.message.clear_recv_buffer()
        for i in range(self.retries):
            mavutil.param_fetch_one(param_name)
            try:
                param_message = self._amavlink.message.get(strmatch=param_name, blocking=True)
            except AMavlinkMessageNotReceivedError:
                param_message = None
                self.logger.warning('AMavlinkParam: Unable to get param {}. Retrying.'.format(param_name))
            if param_message is not None:
                break
            time.sleep(self.retry_delay)
        if param_message is None:
            self.logger.warning('AMavlinkParam: Unable to receive param_message for {}'.format(param_name))
            raise AMavlinkParamNotReceiveError('param name: {}'.format(param_name))
        self.logger.debug('AMavlinkParam: Received message to get param {}: {}'.format(param_name, param_message))
        return param_message.param_value
