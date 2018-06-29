import time


class AMavlinkLocation():

    def __init__(self, amavlink):
        self._amavlink = amavlink
        self._last_update_ts = 0
        self._update_interval = 2  # seconds

    def get_lat(self):
        return self._get_location().lat

    def get_lon(self):
        return self._get_location().lng

    def get_alt(self):
        return self._get_location().alt

    def _get_location(self):
        if time.time() - self._last_update_ts > self._update_interval:
            mavutil = self._amavlink.get_mavutil()
            self._location = mavutil.location()  # TODO since location is blocking a second thread for the timeout has to be added
            self._last_update_ts = time.time()
        return self._location
