class AMavlinkParameter(object):

    def __init__(self, param_message=None, param_name=None, param_value=None):
        self._param_message = param_message
        self._name = param_name
        self._value = param_value

    @property
    def name(self):
        if self._name is None:
            self._name = self._param_message.param_id
        return self._name

    @property
    def value(self):
        if self._value is None:
            self._value = self._param_message.param_value
        return self._value

    @property
    def param_count(self):
        return self._param_message.param_count

    @property
    def index(self):
        return self._param_message.param_index
