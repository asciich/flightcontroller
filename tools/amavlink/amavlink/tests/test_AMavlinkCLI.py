import pytest

from AMavlinkCLI import AMavlinkCLI


@pytest.mark.usefixtures("arducopter_sitl")
class TestAMavlinkCLI(object):

    @pytest.fixture
    def amavlink_cli(self):
        return AMavlinkCLI()

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

    def _assert_text_in_output(self, capsys, expected_stdout, expected_stderr=[], count_in_stdout=[]):
        captured = capsys.readouterr()
        stdout = captured.out.decode()
        stderr = captured.err.decode()
        for text in expected_stdout:
            assert text in stdout
        for count_stdout in count_in_stdout:
            assert count_stdout[1] == stdout.count(count_stdout[0])
        for text in expected_stderr:
            assert text in stderr

    def test_help_page_if_no_param_given(self, amavlink_cli, capsys):
        with pytest.raises(SystemExit) as system_exit:
            amavlink_cli.main([])
        self._assert_system_exit_shows_help(system_exit, capsys)

    def test_get_param(self, amavlink_cli, amavlink, capsys):
        param_name = 'CH7_OPT'
        param_value = 8
        amavlink.param.set(param_name, param_value)
        assert param_value == amavlink.param.get(param_name)

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
        read_value = amavlink.param.get(param_name)
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
        self._assert_text_in_output(capsys, expected_text)

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
        self._assert_text_in_output(capsys, expected_stdout=expected_texts)

    def test_verify_params_from_file_fails(self, amavlink, amavlink_cli, capsys, param_channels_file):
        amavlink.param.set('CH7_OPT', 7)
        amavlink.param.set('CH8_OPT', 7)

        assert 1 == amavlink_cli.main(['paramfile', '--verify', param_channels_file])

        expected_texts = [
            'CH8_OPT 8 != 7.0 verification ERROR!',
        ]
        self._assert_text_in_output(capsys, expected_stdout=expected_texts)

    @pytest.mark.xfail(reason='TODO implement')
    def test_verify_params_from_multible_files(self, amavlink_cli):
        assert False

    @pytest.mark.xfail(reason='TODO implement')
    def test_verify_params_from_multible_files_fails(self, amavlink_cli):
        assert False

    def test_reset_eeprom(self, amavlink, amavlink_cli, capsys):

        assert 0 == amavlink_cli.main(['eeprom', '--reset-default-values'])

        expected_text = [
            'Flightcontroller prepared for resetting EEPROM',
            'Reboot Flightcontroller to reset EEPROM'
        ]
        self._assert_text_in_output(capsys, expected_stdout=expected_text)
        assert 0 == amavlink.param.get('SYSID_SW_MREV')

    def test_enable_debug_log_output(self, amavlink_cli, capsys):
        assert 0 == amavlink_cli.main(['param', '--debug', '--get', 'CH7_OPT'])

        expected_stdout = [
            'Get param "CH7_OPT" = ',
        ]
        expected_stderr = [
            'DEBUG',
            'AMavlinkMessage:',
            'amavlink_logger - INFO - Get param "CH7_OPT" == ',
        ]
        self._assert_text_in_output(capsys=capsys, expected_stdout=expected_stdout, expected_stderr=expected_stderr)

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
        self._assert_text_in_output(capsys, expected_stdout=expected_text, count_in_stdout=count_in_stdout)
