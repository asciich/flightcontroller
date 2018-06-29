import time

import pytest

from AMavlinkErrors import AMavlinkMessageNotReceivedError

@pytest.mark.usefixtures("arducopter_sitl")
class TestAMavlinkMessages(object):

    @pytest.fixture
    def test_timeout(self):
        return 5

    def test_clear_recv_buffer(self, amavlink, is_python3):
        if is_python3:
            expected_error_object = AMavlinkMessageNotReceivedError
        else:
            expected_error_object = Exception
        amavlink.message.clear_recv_buffer()
        with pytest.raises(expected_error_object):
            amavlink.message.get()

    @pytest.mark.xfail(reason='TODO implement')
    @pytest.mark.parametrize('timeout', [
        0.5,
        1,
        1.5
    ])
    def test_get_timeout(self, amavlink, timeout):
        type = 'NONEXISTING_PACKAGE_TYPE'
        relative_error_allowed = 0.01
        t_start = time.time()
        amavlink.message.get(type=type, timeout=timeout, blocking=True)
        elapsed_time = time.time() - t_start
        assert timeout * (1.0 - relative_error_allowed) <= elapsed_time <= timeout * (1.0 + relative_error_allowed)

    def test_get_arbitrary_message(self, amavlink, arducopter_sitl):
        message_received = False
        expected_error_object = AMavlinkMessageNotReceivedError
        if not amavlink.is_python3:
            expected_error_object = Exception
        for i in range(20):
            try:
                if amavlink.message.get() is not None:
                    message_received = True
                    break
            except expected_error_object:
                pass
            time.sleep(0.1)
        assert amavlink.target_id != 0
        assert message_received

    def test_get_message_by_type(self, amavlink, test_timeout):
        message = amavlink.message.get(type='SYSTEM_TIME', blocking=True, timeout=test_timeout)
        assert 0 < message.time_unix_usec
        assert 0 < message.time_boot_ms

    @pytest.mark.parametrize('search_str', [
        'SCALED_IMU2',
        'SYS_STATUS',
        'POWER_STATUS',
        'MEMINFO',
        'MISSION_CURRENT',
        'GPS_RAW_INT',
    ])
    def test_get_message_by_string_match(self, amavlink, search_str, test_timeout):
        message = amavlink.message.get_str_match(search_str=search_str, blocking=True, timeout=test_timeout)
        assert search_str == message.get_type()

    def test_get_system_time(self, amavlink):
        message = amavlink.message.get_system_time()
        assert 0 < message.time_unix_usec
        assert 0 < message.time_boot_ms
