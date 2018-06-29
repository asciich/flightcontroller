


class AMavlinkEeprom(object):

    def __init__(self, amavlink):
        self._amavlink = amavlink

    def prepare_reset_to_default_parameters(self):
        self._amavlink.param.set('SYSID_SW_MREV', 0)
