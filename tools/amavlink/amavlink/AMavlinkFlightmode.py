class AMavlinkFlightmode():

    def __init__(self, amavlink):
        self._amavlink = amavlink

    def set_mode_manual(self):
        mavutil = self._amavlink.get_mavutil()
        mavutil.set_mode_manual()
