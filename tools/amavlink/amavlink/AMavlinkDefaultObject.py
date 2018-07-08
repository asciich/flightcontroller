import sys
import time

from AMavlinkEnums import AMavlinkEnums


class AMavlinkDefaultObject(object):

    def __init__(self, amavlink=None):
        self._default_timeout = 3
        self._default_retries = 10
        self._default_retry_delay = 0.5
        self._enums = AMavlinkEnums()
        if amavlink is not None:
            self.logger = amavlink.get_logger()

    @property
    def is_python3(self):
        if sys.version_info.major == 3:
            return True
        else:
            return False

    @property
    def retries(self):
        return self._default_retries

    @property
    def retry_delay(self):
        return self._default_retry_delay

    def sleep_retry_delay(self):
        time.sleep(self.retry_delay)

    @property
    def timeout(self):
        return self._default_timeout
