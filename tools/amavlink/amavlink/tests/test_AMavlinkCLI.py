import pytest

from AMavlinkPramFile import AMavlinkParamFile
from HelperFunctions import assert_text_in_output


@pytest.mark.usefixtures("arducopter_sitl")
class TestAMavlinkCLI(object):

    @pytest.fixture
    def param_channels_file(self, tmpdir):
        param_path = tmpdir.mkdir('param_files').join('file.param').strpath
        with open(param_path, 'w') as f:
            f.write('CH7_OPT=7\n')
            f.write('CH8_OPT=8\n')
        return param_path

    def _assert_system_exit_shows_help(self, system_exit, capsys):
        assert SystemExit == system_exit.type
        assert 2 == system_exit.value[0]
        captured_output = capsys.readouterr()
        assert 0 == len(captured_output.out)
        assert 'usage:' in captured_output.err.decode()

    def test_help_page_if_no_param_given(self, amavlink_cli, capsys):
        with pytest.raises(SystemExit) as system_exit:
            amavlink_cli.main([])
        self._assert_system_exit_shows_help(system_exit, capsys)

    def test_get_param(self, amavlink_cli, amavlink, capsys):
        param_name = 'CH7_OPT'
        param_value = 8
        amavlink.param.set(param_name, param_value)
        assert param_value == amavlink.param.get_value(param_name=param_name)

        assert 0 == amavlink_cli.main(['param', '--get', param_name])
        expected_output = 'Get param "{}" = {}'.format(param_name, param_value)
        assert expected_output in capsys.readouterr().out.decode()

    def test_get_fails_without_param_name(self, amavlink_cli, capsys):
        with pytest.raises(SystemExit) as system_exit:
            amavlink_cli.main(['param', '--get'])
        self._assert_system_exit_shows_help(system_exit, capsys)

    @pytest.mark.parametrize('param_name, param_value', [
        ('CH7_OPT', 7),
        ('CH7_OPT', 8),
        ('AUTOTUNE_AGGR', 0.05),
        ('AUTOTUNE_AGGR', 0.055),
        ('AUTOTUNE_AGGR', 0.06),
        ('AUTOTUNE_AGGR', 0.07),
        ('AUTOTUNE_AGGR', 0.08),
        ('AUTOTUNE_AGGR', 0.09),
        ('AUTOTUNE_AGGR', 0.095),
        ('AUTOTUNE_AGGR', 0.1),
    ])
    def test_set_param_cli(self, amavlink, amavlink_cli, capsys, param_name, param_value):
        assert 0 == amavlink_cli.main(['param', '--set', param_name, str(param_value)])
        read_value = amavlink.param.get_value(param_name=param_name)
        assert amavlink.param.compare_values_equal(param_value, read_value)

        stdout = capsys.readouterr().out.decode()
        expected_outputs = [
            'Set param "{}" = {}'.format(param_name, param_value),
            '{} {} == {} verified.'.format(param_name, param_value, read_value),
        ]
        for expected_output in expected_outputs:
            assert expected_output in stdout

    def test_upload_params_from_file(self, amavlink, amavlink_cli, capsys, param_channels_file):
        params = ['CH7_OPT', 'CH8_OPT']
        for param in params:
            amavlink.param.set(param, 6)

        assert 0 == amavlink_cli.main(['paramfile', '--upload', param_channels_file])

        expected_text = ['2 params uploaded']
        expected_text.extend(params)
        assert_text_in_output(capsys, expected_text)

    @pytest.mark.xfail(reson='TODO implement')
    def test_upload_and_verify_params_from_file(self, amavlink, amavlink_cli, tmpdir, capsys):
        assert False

    @pytest.mark.xfail(reason='TODO implement')
    def test_upload_params_from_file_fails_if_no_file_specified(self, amavlink_cli):
        assert False

    @pytest.mark.xfail(reason='TODO implement')
    def test_upload_params_from_file_fails_if_file_does_not_exists(self, amavlink_cli):
        assert False

    @pytest.mark.xfail(reason='TODO implement')
    def test_upload_params_from_multible_files(self, amavlink_cli):
        assert False

    def test_verify_params_from_file(self, amavlink, amavlink_cli, capsys, param_channels_file):
        amavlink.param.set('CH7_OPT', 7)
        amavlink.param.set('CH8_OPT', 8)

        assert 0 == amavlink_cli.main(['paramfile', '--verify', param_channels_file])

        expected_texts = [
            'CH7_OPT 7 == 7.0 verified.',
            'CH8_OPT 8 == 8.0 verified.',
            '2 params verified',
        ]
        assert_text_in_output(capsys, expected_stdout=expected_texts)

    def test_verify_params_from_file_fails(self, amavlink, amavlink_cli, capsys, param_channels_file):
        amavlink.param.set('CH7_OPT', 7)
        amavlink.param.set('CH8_OPT', 7)

        assert 1 == amavlink_cli.main(['paramfile', '--verify', param_channels_file])

        expected_texts = [
            'CH8_OPT 8 != 7.0 verification ERROR!',
        ]
        assert_text_in_output(capsys, expected_stdout=expected_texts)

    @pytest.mark.xfail(reason='TODO implement')
    def test_verify_params_from_multible_files(self, amavlink_cli):
        assert False

    @pytest.mark.xfail(reason='TODO implement')
    def test_verify_params_from_multible_files_fails(self, amavlink_cli):
        assert False

    def test_save_all_parameters_to_file(self, amavlink, amavlink_cli, tmpdir, capsys):
        param_path = tmpdir.mkdir('param_files').join('all_params.param').strpath
        param_name = 'CH7_OPT'
        param_value = 9.0
        note_str = 'Automated test for downloading all parameters as file'

        amavlink.param.set(param_name, param_value)
        assert param_value == amavlink.param.get_value(param_name)

        amavlink_cli.main(['paramfile', '--save-all', param_path, '--note', note_str])
        with open(param_path) as f:
            param_file_content = f.read()
        param_file_lines = param_file_content.splitlines()

        n_params = amavlink.param.get_number_of_params()
        n_headers = 3
        assert n_params + n_headers == len(param_file_lines)

        param_file = AMavlinkParamFile(param_path)
        param_file.read()

        assert 850 == len(param_file)
        assert float(param_value) == float(param_file[param_name])

        expected_text = [
            'All parameters written to {}.'.format(param_path),
            'Downloading 10 of 850 parameters.',
            'Downloading 800 of 850 parameters.',
            '850 parameters downloaded.',
        ]
        assert_text_in_output(capsys, expected_stdout=expected_text)

    def test_reset_eeprom(self, amavlink, amavlink_cli, capsys):

        assert 0 == amavlink_cli.main(['eeprom', '--reset-default-values'])

        expected_text = [
            'Flightcontroller prepared for resetting EEPROM',
            'Reboot Flightcontroller to reset EEPROM'
        ]
        assert_text_in_output(capsys, expected_stdout=expected_text)
        assert 0 == amavlink.param.get_value(param_name='SYSID_SW_MREV')

    def test_enable_debug_log_output(self, amavlink_cli, capsys):
        assert 0 == amavlink_cli.main(['param', '--debug', '--get', 'CH7_OPT'])

        expected_stdout = [
            'Get param "CH7_OPT" = ',
        ]
        expected_stderr = [
            'DEBUG',
            'AMavlinkMessage:',
            'amavlink_logger - INFO - Get param value "CH7_OPT" == ',
        ]
        assert_text_in_output(capsys=capsys, expected_stdout=expected_stdout, expected_stderr=expected_stderr)

    def test_get_messages_strmatch(self, amavlink_cli, capsys):
        strmatch = 'GPS_RAW_INT'
        nmsg = 3
        assert 0 == amavlink_cli.main(['messages', '--strmatch', strmatch, '--nmsg', str(nmsg)])

        expected_text = [
            'Capturing messages matching "{}"'.format(strmatch),
            'time_usec',
        ]
        count_in_stdout = [
            (strmatch, nmsg + 1)
        ]
        assert_text_in_output(capsys, expected_stdout=expected_text, count_in_stdout=count_in_stdout)
