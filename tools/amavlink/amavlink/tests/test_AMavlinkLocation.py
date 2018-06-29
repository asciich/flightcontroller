import pytest


@pytest.mark.skip(msg='TODO implement')
class TestAMavlinkLocation(object):

    def test_get_location(self, amavlink, arducopter_sitl):
        assert -35.3632608 == amavlink.location.get_lat()
        assert 149.1652351 == amavlink.location.get_lon()

    @pytest.mark.xfail(reason='Todo')
    def test_get_altitude(self, amavlink, arducopter_sitl):
        assert 0.0 <= amavlink.location.get_alt() <= 0.5

    @pytest.mark.skip()
    def test_get_location_not_reachable_error(self, amavlink_unconnected):
        # Todo should raise an error
        amavlink_unconnected.location.get_lat()
        amavlink_unconnected.location.get_lon()
        amavlink_unconnected.location.get_alt()
