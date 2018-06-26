import pytest

from AMavlinkDefaultObject import AMavlinkDefaultObject
from AMavlinkEnums import AMavlinkEnums


class TestAMavlinkDefaultObject(object):

    @pytest.fixture
    def amavlink_default_object(self):
        return AMavlinkDefaultObject()

    def test_default_retries(self, amavlink_default_object):
        assert 10 == amavlink_default_object.retries

    def test_default_timeout(self, amavlink_default_object):
        assert 3 == amavlink_default_object.timeout

    def test_retry_delay(self, amavlink_default_object):
        assert 0.5 == amavlink_default_object.retry_delay

    def test_enums_available(self, amavlink_default_object):
        assert isinstance(amavlink_default_object._enums, AMavlinkEnums)
