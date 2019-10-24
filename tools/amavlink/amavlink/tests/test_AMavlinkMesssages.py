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
        for i in range(3):
            # Since this test case relies on no messages sent in between,
            # it is repeated 3 times.
            amavlink.message.clear_recv_buffer()
            try:
                amavlink.message.get()
            except expected_error_object:
                return
        assert False

    @pytest.mark.parametrize('timeout', [
        1,
        1.5
    ])
    def test_get_messages_timeout(self, amavlink, timeout):
        type = 'NONEXISTING_PACKAGE_TYPE'
        relative_error_allowed = 0.2
        amavlink.message.clear_recv_buffer()
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
        assert search_str == message.get_type

    def test_get_system_time(self, amavlink):
        message = amavlink.message.get_system_time()
        assert 0 < message.time_unix_usec
        assert 0 < message.time_boot_ms
