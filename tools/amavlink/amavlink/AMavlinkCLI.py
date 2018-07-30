#!/usr/bin/env python2

import argparse
import sys
import time

from AMavlink import AMavlink
from AMavlinkDefaultObject import AMavlinkDefaultObject
from AMavlinkErrors import AMavlinkCLIParseError, AMavlinkCLIParamVerificationError, AMavlinkMessageNotReceivedError
from AMavlinkPramFile import AMavlinkParamFile


class AMavlinkCLI(AMavlinkDefaultObject):

    def __init__(self):
        super(AMavlinkCLI, self).__init__()

    def main(self, argv):
        parser = argparse.ArgumentParser(description='AMavlink CLI for Mavlink communication.')
        subparsers = parser.add_subparsers(help='Main commands')

        eeprom_parser = subparsers.add_parser('eeprom', help='Handle eeprom')
        eeprom_parser.add_argument('--debug', default=False, action='store_true', help='Enable debug output')
        eeprom_parser.add_argument('--reset-default-values', action='store_true', help='Reset flightcontroller EEPROM')

        messages_parser = subparsers.add_parser('messages', help='Receive MAVLink messages')
        messages_parser.add_argument('--debug', default=False, action='store_true', help='Enable debug output')
        messages_parser.add_argument('--strmatch', help='Filter messages only matching given string')
        messages_parser.add_argument('--nmsg', type=int, default=-1, help='Stop after n messages.')

        param_parser = subparsers.add_parser('param', help='Manipulate parameters')
        param_parser.add_argument('--debug', default=False, action='store_true', help='Enable debug output')
        param_parser.add_argument('--get', help='Get a parameter value')
        param_parser.add_argument('--set', nargs=2, help='Set a parameter. Syntax: "--set PARAM_NAME VALUE"')

        paramfile_parser = subparsers.add_parser('paramfile', help='Handle param files')
        paramfile_parser.add_argument('--debug', default=False, action='store_true', help='Enable debug output.')
        paramfile_parser.add_argument('--note', default='', help='Add note to downloaded parameters file.')
        paramfile_parser.add_argument('--save-all', help='Save all parameters to file.')
        paramfile_parser.add_argument('--upload', nargs='+', help='Upload all parameters in a file.')
        paramfile_parser.add_argument('--verify', nargs='+', help='Verify parameters in a file.')

        tune_parser = subparsers.add_parser('tune', help='Handle manual tuning with channel6 knob.')
        tune_parser.add_argument('--debug', default=False, action='store_true', help='Enable debug output.')
        tune_parser.add_argument('--disable', default=False, action='store_true', help='Disable manual tuning.')
        tune_parser.add_argument('--rate-roll-pitch-kp', default=False, action='store_true',
                                 help='Tune "Rate Roll/Pitch kP"')
        tune_parser.add_argument('--rate-roll-pitch-ki', default=False, action='store_true',
                                 help='Tune "Rate Roll/Pitch kI"')
        tune_parser.add_argument('--rate-roll-pitch-kd', default=False, action='store_true',
                                 help='Tune "Rate Roll/Pitch kD"')
        tune_parser.add_argument('--rate-yaw-kp', default=False, action='store_true',
                                 help='Tune "Rate Yaw kP"')
        tune_parser.add_argument('--rate-yaw-kd', default=False, action='store_true',
                                 help='Tune "Rate Yaw kD"')
        tune_parser.add_argument('--n_refresh', default=0,
                                 help='Number of refreshes of actual tuning state. 0 means until AMavlink is stopped')

        if len(argv) == 1:
            parser.print_help()
            exit(2)

        args = parser.parse_args(args=argv)
        self._amavlink = AMavlink(debug_log_to_console=args.debug)
        self.logger = self._amavlink.logger
        self.logger.debug('AMavlinkCLI parameters {}'.format(argv))
        if argv[0] == 'eeprom':
            return self._run_eeprom(args)
        elif argv[0] == 'messages':
            return self._run_messages(args)
        elif argv[0] == 'param':
            return self._run_param(args)
        elif argv[0] == 'paramfile':
            return self._run_paramfile(args)
        elif argv[0] == 'tune':
            return self._run_tune(args)
        else:
            AMavlinkCLIParseError()
        return 0

    def _run_eeprom(self, args):
        if args.reset_default_values:
            self._amavlink.eeprom.prepare_reset_to_default_parameters()
            print('Flightcontroller prepared for resetting EEPROM')
            print('Reboot Flightcontroller to reset EEPROM')
        else:
            raise AMavlinkCLIParseError()
        return 0

    def _run_messages(self, args):
        nmsg = args.nmsg

        if args.strmatch is not None:
            strmatch = args.strmatch
            print('Capturing messages matching "{}"'.format(strmatch))
            msg_counter = 0
            while True:
                try:
                    msg = self._amavlink.message.get(strmatch=strmatch)
                    print(msg)
                    msg_counter += 1
                except AMavlinkMessageNotReceivedError:
                    self.sleep_retry_delay()
                if nmsg > 0:
                    if msg_counter >= nmsg:
                        return 0
        else:
            raise AMavlinkCLIParseError()
        return 0

    def _run_param(self, args):
        if args.get is not None:
            param_name = args.get
            param_value = self._amavlink.param.get_value(param_name=param_name)
            print('Get param "{}" = {}'.format(param_name, param_value))

        elif args.set is not None:
            param_name = args.set[0]
            param_value = args.set[1]
            self._set_param(param_name, param_value)
            try:
                self._verify_param(param_name, param_value)
            except AMavlinkCLIParamVerificationError:
                return 1
        else:
            raise AMavlinkCLIParseError()
        return 0

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
                    try:
                        self._verify_param(param_name, param_value)
                    except AMavlinkCLIParamVerificationError:
                        return 1
                    param_counter += 1
            print('{} params verified.'.format(param_counter))
        elif args.save_all is not None:
            param_path = args.save_all

            def download_params_progress(actual_param, total_params):
                if actual_param % 10 == 0:
                    print('Downloading {} of {} parameters.'.format(actual_param, total_params))

            all_params = self._amavlink.param.get_all(progress_function=download_params_progress)
            print('{} parameters downloaded.'.format(len(all_params)))
            param_file = AMavlinkParamFile(param_path)
            param_file.add_parameters(all_params)
            if args.note is not None:
                param_file.add_note(args.note)
            param_file.write()
            print('All parameters written to {}.'.format(param_path))
        else:
            raise AMavlinkCLIParseError()
        return 0

    def _run_tune(self, args):
        n_refresh = args.n_refresh
        if args.disable:
            self._amavlink.tune.disable()
            print('Manual tuning disalbed')
        elif args.rate_roll_pitch_kp:
            self._tune_param(self._amavlink.tune.RATEROLL_PITCH_KP, n_refresh)
        elif args.rate_roll_pitch_ki:
            self._tune_param(self._amavlink.tune.RATEROLL_PITCH_KI, n_refresh)
        elif args.rate_roll_pitch_kd:
            self._tune_param(self._amavlink.tune.RATEROLL_PITCH_KD, n_refresh)
        elif args.rate_yaw_kp:
            self._tune_param(self._amavlink.tune.RATE_YAW_KP, n_refresh)
        elif args.rate_yaw_kd:
            self._tune_param(self._amavlink.tune.RATE_YAW_KD, n_refresh)
        else:
            raise AMavlinkCLIParseError('No action for manual tuning defined')
        return 0

    def _set_param(self, param_name, param_value):
        self._amavlink.param.set(param_name, param_value)
        print('Set param "{}" = {}'.format(param_name, param_value))

    def _tune_param(self, tune_parameter, n_refresh):
        n_refresh = int(n_refresh)
        if n_refresh == 0:
            n_refresh = -1

        print('Start tuning {}'.format(tune_parameter))
        self._amavlink.tune.manual_tuning(tune_parameter)

        error_counter = 0
        retry_delay = 1.0
        while n_refresh != 0:
            try:
                t_start = time.time()
                tune = self._amavlink.tune
                original_value = tune.get_original_value()
                actual_value = tune.get_actual_tune_value()
                param_name = tune.get_actual_tune_param_name()
                range = tune.get_tune_range()
                tune_knob_pwm = tune.get_tune_knob_pwm()
                error_counter = 0

                tune_msg = 'Tune {}; actual_value = {}; tune_knob_pwm = {}; original_value = {}; range = {}'.format(
                    param_name, actual_value, tune_knob_pwm, original_value, range)
                self.logger.info(tune_msg)
                print(tune_msg)
                t_refresh = time.time() - t_start
                if t_refresh > retry_delay:
                    self.logger.warning(
                        '_tune_param refresh takes longer ({}s) than retry_delay={}s'.format(t_refresh, retry_delay))
                    t_wait = 0.0
                else:
                    t_wait = retry_delay - t_refresh

            except Exception as e:
                self.logger.warning('Refresh tune parameter failed with exception: {}'.format(e))
                print('Refresh failed')
                t_wait = retry_delay / 3

                if error_counter == 3:
                    n_refresh -= 1
                    error_counter = 0
                else:
                    error_counter += 1
                    n_refresh += 1

            if n_refresh > 0:
                n_refresh -= 1
            time.sleep(t_wait)

    def _verify_param(self, param_name, param_value):
        read_value = self._amavlink.param.get_value(param_name=param_name)
        if self._amavlink.param.compare_values_equal(param_value, read_value):
            print('{} {} == {} verified.'.format(param_name, param_value, read_value))
        else:
            error_message = '{} {} != {} verification ERROR!'.format(param_name, param_value, read_value)
            print(error_message)
            raise AMavlinkCLIParamVerificationError(error_message)


def main():
    amavlink_cli = AMavlinkCLI()
    return amavlink_cli.main(sys.argv[1:])


if __name__ == '__main__':
    exit(main())
