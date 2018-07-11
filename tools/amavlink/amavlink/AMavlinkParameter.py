class AMavlinkParameter(object):

    def __init__(self, param_message):
        self._param_message = param_message

    @property
    def name(self):
        return self._param_message.param_id

    @property
    def value(self):
        return self._param_message.param_value

    @property
    def param_count(self):
        return self._param_message.param_count

    @property
    def index(self):
        return self._param_message.param_index
