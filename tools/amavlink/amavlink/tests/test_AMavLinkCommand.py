import pytest


class TestAMAvlinkCommand():

    @pytest.mark.skip('TODO implement')
    def test_preflight_stroage_read_params_from_flash(self, amavlink):
        param_name = 'CH7_OPT'
        param_value = amavlink.param.get(param_name)
        ram_value = param_value + 1.0
        amavlink.param.set(param_name, ram_value)
        assert ram_value == amavlink.param.get(param_name)

        # TODO this should raise a not implemented error
        amavlink.command.preflight_storage_read_params_from_flash()

        assert param_value == amavlink.param.get(param_name)
