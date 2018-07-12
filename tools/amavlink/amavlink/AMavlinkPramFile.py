import datetime

from AMavlinkErrors import AMavlinkParamFileDelimiterNotFoundInLineError, AMavlinkParamFileWriteEmptyFileError
from AMavlinkParameter import AMavlinkParameter


class AMavlinkParamFile(object):

    def __init__(self, path):
        self._path = path
        self._parameters = None
        self._default_section = 'AMAvlinkParamFile DEFAULT CONFIG SECTION'
        self._delimiters = ['=', ',', ':']
        self._codeblock_marker = '```'
        self.note = ''

    def __getitem__(self, item):
        return self._parameters[item]

    # Needed to make AMavlink interable
    def __iter__(self):
        return iter(self._parameters)

    # Needed to make AMavlink interable
    def keys(self):
        return self._parameters.keys()

    # Needed to make AMavlink interable
    def items(self):
        return self._parameters.items()

    # Needed to make AMavlink interable
    def values(self):
        return self._parameters.values()

    def __len__(self):
        return len(self._parameters)

    def add_note(self, note_str):
        self.note = note_str

    def add_parameter(self, param, param_value):
        if self._parameters is None:
            self._parameters = {}
        self._parameters[param] = param_value

    def add_parameters(self, parameters):
        for param_name in parameters:
            param_value = parameters[param_name]
            if isinstance(param_value, AMavlinkParameter):
                param_value = param_value.value
            self.add_parameter(param_name, param_value)

    def read(self):
        file_content = open(self._path, 'r').read()
        if self._codeblock_marker in file_content:
            file_content = self._extract_code_blocks(file_content)
            file_content = self._remove_command_lines(file_content)
        file_content = self._remove_comments(file_content)
        self._parameters = self._extract_parameters(file_content)
        self._note = ''

    def write(self):
        if self._parameters is None:
            raise AMavlinkParamFileWriteEmptyFileError()
        if len(self._parameters) == 0:
            raise AMavlinkParamFileWriteEmptyFileError()
        self._write_header()
        self._write_param_lines()

    def _write_header(self):
        with open(self._path, 'w') as f:
            f.write('#Date: {}\n'.format(str(datetime.datetime.now())))
            if len(self.note) > 0:
                f.write('#Note: {}\n'.format(self.note))
            f.write('#Note: Created by amavlink\n')

    def _write_param_lines(self):
        param_lines = []
        for param_name in self._parameters:
            param_lines.append('{}, {}\n'.format(param_name, self[param_name]))
        param_lines = sorted(param_lines)
        with open(self._path, 'a') as f:
            for param_line in param_lines:
                f.write(param_line)

    def _get_delimiter_in_line(self, file_line):
        smallest_index = len(file_line)
        delimiter = None
        for d in self._delimiters:
            try:
                index = file_line.index(d)
            except ValueError:
                continue
            if index < smallest_index:
                smallest_index = index
                delimiter = d
        if delimiter is None:
            raise AMavlinkParamFileDelimiterNotFoundInLineError(file_line)
        return delimiter

    def _extract_code_blocks(self, file_content):
        codeblock_content = ''
        is_inside_codeblock = False
        for line in file_content.splitlines():
            line = line.strip()
            if self._line_starts_with_inline_codeblock(line):
                continue
            if is_inside_codeblock:
                if line.startswith(self._codeblock_marker):
                    is_inside_codeblock = False
                    continue
                else:
                    codeblock_content += '{}\n'.format(line)
            else:
                if line.startswith(self._codeblock_marker):
                    is_inside_codeblock = True
                    continue
        return codeblock_content

    def _extract_parameters(self, file_content):
        config = {}
        for line in file_content.splitlines():
            line = line.strip()
            if len(line) == 0:
                continue
            delimiter = self._get_delimiter_in_line(line)
            delimiter_index = line.index(delimiter)
            name = line[:delimiter_index].strip()
            value = line[delimiter_index + 1:].strip()
            if name.count(' ') > 0:
                continue
            config[name] = value
        return config

    def _line_starts_with_inline_codeblock(self, line):
        line = line.strip()
        if line.startswith(self._codeblock_marker):
            line = line.replace(self._codeblock_marker, '', 1)
            if self._codeblock_marker in line:
                return True
        return False

    def _remove_command_lines(self, file_content):
        param_lines = ''
        for line in file_content.splitlines():
            try:
                delimiter_index = self._get_delimiter_in_line(line)
            except AMavlinkParamFileDelimiterNotFoundInLineError:
                continue
            param_lines += '{}\n'.format(line)
        return param_lines

    def _remove_comments(self, file_content):
        result = ''
        for line in file_content.splitlines():
            if line.count('#') > 0:
                line = line[:line.index('#')]
            line = line.strip()
            if len(line) == 0:
                continue
            result += line + '\n'
        return result
