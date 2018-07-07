import pytest

from AMavlinkErrors import AMavlinkParamVerificationError


@pytest.mark.usefixtures("arducopter_sitl")
class TestAMavlinkParam(object):

    @pytest.fixture()
    def param_file(self, tmpdir):
        p = tmpdir.mkdir('param_files').join('set_param_from_file.param')
        path = p.strpath
        with open(path, 'w') as f:
            f.write('CH7_OPT=11\n')
            f.write('CH8_OPT=12\n')
        return path

    @pytest.mark.parametrize('param_name,param_value', [
        ('CH7_OPT', 9),
        (b'CH7_OPT', 8),
        ('CH7_OPT', '7'),
        ('RC11_REVERSED', 0),
    ])
    def test_set_and_get_param(self, amavlink, param_name, param_value):
        amavlink.param.set(param_name, param_value)
        assert float(param_value) == amavlink.param.get(param_name)

    def test_get_param_several_times(self, amavlink):
        param_name = 'CH7_OPT'
        param_value = '7'
        amavlink.param.set(param_name, param_value)
        for i in range(5):
            assert float(param_value) == amavlink.param.get(param_name)

    def test_set_param_from_file(self, amavlink, param_file):
        amavlink.param.set_from_file(path=param_file)
        assert amavlink.param.verify_from_file(path=param_file)

    def test_set_param_from_file_fails(self, amavlink, tmpdir, is_python3):

        if is_python3:
            expected_error_object = AMavlinkParamVerificationError
        else:
            expected_error_object = Exception

        p = tmpdir.mkdir('param_files').join('set_param_from_file_fails.param')
        path = p.strpath
        with open(path, 'w') as f:
            f.write('CH7_OPT=13\n')
            f.write('CH8_OPT=14\n')
        amavlink.param.set_from_file(path=path)

        with open(path, 'w') as f:
            f.write('CH7_OPT=13\n')
            f.write('CH8_OPT=2\n')
        with pytest.raises(expected_error_object):
            amavlink.param.verify_from_file(path=path)

    def test_verify_param_from_file(self, amavlink, param_file):
        amavlink.param.set_from_file(path=param_file)
        amavlink.param.verify_from_file(path=param_file)

    @pytest.mark.parametrize('val1, val2, equal', [
        (1.1, 1, False),
        (0.000001, 0.0000001, False),
        (0.0, 0.1, False),
        (0.1, 0.0, False),
        (0.0, 0.0, True),
        (1, 1, True),
        (1.0, 1, True),
        ('1', '1.0', True),
        (1, '1.0', True),
        ('1', '1.0', True),
        ('1', '1', True),
        ('1.0', 1, True),
        (-1, 1, False),
        (10.43334961, 10.4333496094, True),
        (0.10000000149, 0.1, True),
        (0.10000000149, -0.1, False),
        (1.01000003815, 1.01, True),
        (10.1000003815, 10.1, True),
        (101.000003815, 101.0, True),
        (1010.00003815, 1010.0, True),
        (10100.0003815, 10100.0, True),
        (10.1000003815, -10.1, False),
        (-10.1000003815, 10.1, False),
        (1.0 + 3.9e-8, 1, True),
        (1.0 + 4.1e-8, 1, False),
    ])
    def test_comapare_equal(self, amavlink, val1, val2, equal):
        assert equal == amavlink.param.compare_values_equal(val1, val2)
