from AMavlinkErrors import AMavlinkParamFileDelimiterNotFoundInLineError


class AMavlinkParamFile(object):

    def __init__(self, path):
        self._path = path
        self._parameters = None
        self._default_section = 'AMAvlinkParamFile DEFAULT CONFIG SECTION'
        self._delimiters = ['=', ',', ':']
        self._codeblock_marker = '```'

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

    def read(self):
        file_content = open(self._path, 'r').read()
        if self._codeblock_marker in file_content:
            file_content = self._extract_code_blocks(file_content)
            file_content = self._remove_command_lines(file_content)
        file_content = self._remove_comments(file_content)
        self._parameters = self._extract_parameters(file_content)

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
