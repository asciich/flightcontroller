import StringIO

import ConfigParser

class AMavlinkParamFile(object):

    def __init__(self, path):
        self._path = path
        self._parameters = None
        self._default_section = 'AMAvlinkParamFile DEFAULT CONFIG SECTION'

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
        file_content = '[{}]\n'.format(self._default_section) + open(self._path, 'r').read()
        file_content = self._remove_comments(file_content)
        ini_fp = StringIO.StringIO(file_content)
        config = ConfigParser.RawConfigParser()
        config.optionxform = str
        config.readfp(ini_fp)
        self._parameters = dict(config.items(self._default_section))

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
