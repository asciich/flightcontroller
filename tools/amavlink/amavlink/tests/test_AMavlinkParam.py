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

    @pytest.mark.parametrize('param_name,param_value',[
        ('CH7_OPT', 9),
        (b'CH7_OPT', 8),
        ('CH7_OPT', '7'),
        ('RC11_REVERSED' ,0),
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

    def test_set_param_from_file_fails(self, amavlink, tmpdir):
        p = tmpdir.mkdir('param_files').join('set_param_from_file_fails.param')
        path = p.strpath
        with open(path, 'w') as f:
            f.write('CH7_OPT=13\n')
            f.write('CH8_OPT=14\n')
        amavlink.param.set_from_file(path=path)

        with open(path, 'w') as f:
            f.write('CH7_OPT=13\n')
            f.write('CH8_OPT=2\n')
        with pytest.raises(AMavlinkParamVerificationError):
            amavlink.param.verify_from_file(path=path)

    def test_verify_param_from_file(self, amavlink, param_file):
        amavlink.param.set_from_file(path=param_file)
        amavlink.param.verify_from_file(path=param_file)

