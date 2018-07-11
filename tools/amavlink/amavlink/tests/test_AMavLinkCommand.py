import pytest

from AMavlinkErrors import ErrorAMavlinkNoCommandSpecified


@pytest.mark.usefixtures("arducopter_sitl")
class TestAMAvlinkCommand():

    @pytest.mark.skip('TODO implement')
    def test_preflight_stroage_read_params_from_flash(self, amavlink):
        param_name = 'CH7_OPT'
        param_value = amavlink.param.get_value(param_name=param_name)
        ram_value = param_value + 1.0
        amavlink.param.set(param_name, ram_value)
        assert ram_value == amavlink.param.get(param_name)

        # TODO this should raise a not implemented error
        amavlink.command.preflight_storage_read_params_from_flash()

        assert param_value == amavlink.param.get_value(param_name=param_name)

    def test_no_command_specified_error(self, amavlink, is_python3):
        if is_python3:
            expected_error_object = ErrorAMavlinkNoCommandSpecified
        else:
            expected_error_object = Exception  # Pytest in python 2 does not handle custom Error Commands
        with pytest.raises(expected_error_object):
            amavlink.command.send_long()
