import os

import pytest

from AMavlinkErrors import AMavlinkParamFileWriteEmptyFileError
from AMavlinkParameter import AMavlinkParameter
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

    def test_read_param_file(self, param_file_equal_separated):
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
        ',',
        ' , ',
        ':',
        '          :    ',
    ])
    def test_read_param_file_delimiter(self, delimiter, tmpdir):
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
        assert 4 == len(param_file)

    def test_is_iterable(self, param_file_equal_separated):
        param_file = AMavlinkParamFile(param_file_equal_separated)
        param_file.read()
        for param_name in param_file:
            assert param_name in ['CH7_OPT', 'CH8_OPT']

    def test_read_markdown_file(self):
        test_path = os.path.join(os.path.dirname(__file__))
        markdown_path = os.path.join(test_path, '..', '..', 'doc', 'param_file.md')
        markdown_path = os.path.abspath(markdown_path)
        assert os.path.exists(markdown_path)

        param_file = AMavlinkParamFile(markdown_path)
        param_file.read()

        assert '7' == param_file['CH7_OPT']
        assert '8' == param_file['CH8_OPT']
        assert '0' == param_file['RC11_DZ']
        assert 3 == len(param_file)
        assert param_file.note == ''

    def test_write_param_file(self, tmpdir):
        param_path = tmpdir.mkdir('param_files').join('write.param').strpath
        param_file = AMavlinkParamFile(param_path)
        param_file.add_parameter('CH9_OPT', 9)
        note_str = 'Automatically tested'
        parameters = {
            'CH8_OPT': 8,
            'CH7_OPT': 7,
        }
        param_file.add_parameters(parameters)
        self._assert_write_default_file(param_file, param_path, note_str)

    def test_write_param_file_from_all_parameters_dict(self, tmpdir):
        param_path = tmpdir.mkdir('param_files').join('write.param').strpath
        param_file = AMavlinkParamFile(param_path)
        all_params_dict = {
            'CH7_OPT': AMavlinkParameter(param_name='CH7_OPT', param_value=7),
            'CH8_OPT': AMavlinkParameter(param_name='CH8_OPT', param_value=8),
            'CH9_OPT': AMavlinkParameter(param_name='CH9_OPT', param_value=9),
        }
        note_str = 'Automatically tested2'
        param_file.add_parameters(all_params_dict)
        self._assert_write_default_file(param_file, param_path, note_str)

    def _assert_write_default_file(self, param_file, param_path, note_str):
        assert 3 == len(param_file)

        param_file.add_note(note_str)
        assert note_str == param_file.note
        param_file.write()

        with open(param_path) as f:
            param_file_content = f.read()
        param_file_lines = param_file_content.splitlines()
        assert param_file_lines[0].startswith('#Date: ')
        assert '#Note: {}'.format(note_str) == param_file_lines[1].strip()
        assert '#Note: Created by amavlink' == param_file_lines[2].strip()
        assert 'CH7_OPT, 7' == param_file_lines[3].strip()
        assert 'CH8_OPT, 8' == param_file_lines[4].strip()
        assert 'CH9_OPT, 9' == param_file_lines[5].strip()

        assert 6 == len(param_file_lines)

    def test_write_empty_param_file_fails(self, tmpdir, is_python3):
        param_path = tmpdir.mkdir('param_files').join('write.param').strpath
        param_file = AMavlinkParamFile(param_path)

        if is_python3:
            expected_error_object = AMavlinkParamFileWriteEmptyFileError
        else:
            expected_error_object = Exception

        with pytest.raises(expected_error_object):
            param_file.write()

    def test_write_without_note(self, tmpdir):
        param_path = tmpdir.mkdir('param_files').join('write.param').strpath
        param_file = AMavlinkParamFile(param_path)

        param_file.add_parameter('CH7_OPT', '8')
        param_file.write()

        with open(param_path) as f:
            param_file_content = f.read()
        param_file_lines = param_file_content.splitlines()
        assert param_file_lines[0].startswith('#Date: ')
        assert '#Note: Created by amavlink' == param_file_lines[1].strip()
        assert 'CH7_OPT, 8' == param_file_lines[2].strip()

        assert 3 == len(param_file_lines)
