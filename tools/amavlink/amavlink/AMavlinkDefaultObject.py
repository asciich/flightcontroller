from AMavlinkEnums import AMavlinkEnums


class AMavlinkDefaultObject(object):

    def __init__(self):
        self._default_timeout = 3
        self._default_retries = 10
        self._default_retry_delay = 0.5
        self._enums = AMavlinkEnums()

    @property
    def retries(self):
        return self._default_retries

    @property
    def retry_delay(self):
        return self._default_retry_delay

    @property
    def timeout(self):
        return self._default_timeout