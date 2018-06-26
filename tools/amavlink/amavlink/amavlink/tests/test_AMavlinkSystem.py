import time

import pytest


class TestAMavlinkSystem(object):

    def test_uptime(self, amavlink, arducopter_sitl):
        t_uptime_start = amavlink.system.uptime()
        t_start = time.time()
        assert isinstance(t_uptime_start, float)
        assert 0 < t_uptime_start
        time.sleep(1)
        uptime_elapsed = amavlink.system.uptime() - t_uptime_start
        time_elapsed = time.time() - t_start
        allowed_error = 0.07
        assert time_elapsed * (1-allowed_error) <= uptime_elapsed <= time_elapsed * (1+allowed_error)

