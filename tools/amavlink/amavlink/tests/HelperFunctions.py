def assert_text_in_output(capsys, expected_stdout, expected_stderr=[], count_in_stdout=[]):
    captured = capsys.readouterr()
    stdout = captured.out.decode()
    stderr = captured.err.decode()
    for text in expected_stdout:
        assert text in stdout, '{} not found in {}'.format(text, stdout)
    for count_stdout in count_in_stdout:
        assert count_stdout[1] == stdout.count(count_stdout[0])
    for text in expected_stderr:
        assert text in stderr
