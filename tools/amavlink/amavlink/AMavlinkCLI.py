#!/usr/bin/env python2

import argparse

import sys

from AMavlink import AMavlink
from AMavlinkErrors import AMavlinkCLIParseError
from AMavlinkPramFile import AMavlinkParamFile


class AMavlinkCLI(object):

    def __init__(self):
        pass

    def main(self, argv):
        parser = argparse.ArgumentParser(description='AMavlink CLI for Mavlink communication.')
        subparsers = parser.add_subparsers(help='Main commands')

        param_parser = subparsers.add_parser('param', help='Manipulate parameters')
        param_parser.add_argument('--get', help='Get a parameter value')
        param_parser.add_argument('--set', nargs=2,help='Set a parameter. Syntax: "--set PARAM_NAME VALUE"')

        paramfile_parser = subparsers.add_parser('paramfile', help='Handle param files')
        paramfile_parser.add_argument('--upload', nargs='+', help='Upload all parameters in a file')
        paramfile_parser.add_argument('--verify', nargs='+', help='Verify parameters in a file')

        if len(argv) == 1:
            parser.print_help()
            exit(2)

        args = parser.parse_args(args=argv)
        self._amavlink = AMavlink()
        if argv[0] == 'param':
            self._run_param(args)
        elif argv[0] == 'paramfile':
            return self._run_paramfile(args)
        else:
            AMavlinkCLIParseError()
        return 0

    def _run_param(self, args):
        if args.get is not None:
            param_name = args.get
            param_value = self._amavlink.param.get(param_name)
            print('Get param "{}" = {}'.format(param_name, param_value))

        elif args.set is not None:
            param_name = args.set[0]
            param_value = args.set[1]
            self._set_param(param_name, param_value)
            read_value = self._amavlink.param.get(param_name)
            if float(param_value) == float(read_value):
                print('Verified')
            else:
                print('Setting param failed')
                exit(1)
        else:
            raise AMavlinkCLIParseError()

    def _run_paramfile(self, args):
        if args.upload is not None:
            param_counter = 0
            for path in args.upload:
                param_file = AMavlinkParamFile(path)
                param_file.read()
                for param_name in param_file:
                    param_value = param_file[param_name]
                    self._set_param(param_name, param_value)
                    param_counter += 1
            print('{} params uploaded.'.format(param_counter))
        elif args.verify is not None:
            param_counter = 0
            for path in args.verify:
                param_file = AMavlinkParamFile(path)
                param_file.read()
                for param_name in param_file:
                    param_value = param_file[param_name]
                    read_value = self._amavlink.param.get(param_name)
                    if float(param_value) == float(read_value):
                        print('{} {} == {} verified.'.format(param_name, param_value, read_value))
                    else:
                        print('{} {} != {} verification ERROR!'.format(param_name, param_value, read_value))
                        return 1
                    param_counter += 1
            print('{} params verified.'.format(param_counter))
        else:
            raise AMavlinkCLIParseError()
        return 0

    def _set_param(self, param_name, param_value):
        self._amavlink.param.set(param_name, param_value)
        print('Set param "{}" = {}'.format(param_name, param_value))

def main():
    amavlink_cli = AMavlinkCLI()
    exit(amavlink_cli.main(sys.argv[1:]))

if __name__ == '__main__':
    main()