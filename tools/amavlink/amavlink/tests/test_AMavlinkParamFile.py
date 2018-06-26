import pytest

from AMavlinkPramFile import AMavlinkParamFile


class TestAMavlinkParamFile(object):

    @pytest.fixture
    def file_params(self):
        return {
            'CH7_OPT': 9,
            'CH8_OPT': 10,
        }

    @pytest.fixture
    def param_file_equal_separated(self, tmpdir, file_params):
        path = tmpdir.mkdir('param_files').join('file.param').strpath
        with open(path, 'w') as f:
            f.write('# Automatically generated for testing.\n')
            for key in file_params:
                line = '{}={}\n'.format(key, file_params[key])
                f.write(line)
        return path

    def test_read_param_file(self,param_file_equal_separated):
        param_file = AMavlinkParamFile(param_file_equal_separated)
        param_file.read()
        assert 2 == len(param_file)
        assert '9' == param_file['CH7_OPT']
        assert '10' == param_file['CH8_OPT']

    @pytest.mark.parametrize('delimiter', [
        '=',
        ' =',
        '= ',
        ' = ',
        '  =  ',
    ])
    def test_read_param_file_with_spaces(self, delimiter, tmpdir):
        param_path = tmpdir.mkdir('param_files').join('file.param').strpath
        with open(param_path, 'w') as f:
            f.write('CH7_OPT{}8'.format(delimiter))
        param_file = AMavlinkParamFile(param_path)
        param_file.read()
        assert '8' == param_file['CH7_OPT']

    @pytest.mark.parametrize('line', [
        'CH7_OPT = 7#',
        'CH7_OPT = 7 #',
        'CH7_OPT = 7        #',
        'CH7_OPT = 7 # this set CH7_OPT',
        'CH7_OPT = 7 #this set CH7_OPT',
        'CH7_OPT=7 #this set CH7_OPT',
        'CH7_OPT=7 #this #set CH7_OPT',
    ])
    def test_read_param_file_with_inline_comment(self, tmpdir, line):
        param_path = tmpdir.mkdir('param_files').join('file.param').strpath
        with open(param_path, 'w') as f:
            f.write(line)
        param_file = AMavlinkParamFile(param_path)
        param_file.read()
        assert '7' == param_file['CH7_OPT']

    def test_read_param_file_with_multible_comments(self, tmpdir):
        param_path = tmpdir.mkdir('param_files').join('file.param').strpath
        with open(param_path, 'w') as f:
            f.write('#Comment\n')
            f.write('CH7_OPT = 7 # comment\n')
            for i in range(5):
                f.write('#Comment\n')
            f.write('CH8_OPT = 8 #\n')
            f.write('CH9_OPT=9\n')
            f.write('CH10_OPT=10\n')
            for i in range(5):
                f.write('#Comment\n')
        param_file = AMavlinkParamFile(param_path)
        param_file.read()
        assert '7' == param_file['CH7_OPT']
        assert '8' == param_file['CH8_OPT']
        assert '9' == param_file['CH9_OPT']
        assert '10' == param_file['CH10_OPT']

    def test_is_iterable(self, param_file_equal_separated):
        param_file = AMavlinkParamFile(param_file_equal_separated)
        param_file.read()
        for param_name in param_file:
            assert param_name in ['CH7_OPT', 'CH8_OPT']