import time

from AMavlinkDefaultObject import AMavlinkDefaultObject
from AMavlinkErrors import AMavlinkTuneUnableToSetTuneKnob, AmavlinkUnknownTuneParameter


class AMavlinkTune(AMavlinkDefaultObject):

    RATEROLL_PITCH_KP = 'RATE_ROLL_PITCH_KP'
    RATEROLL_PITCH_KI = 'RATE_ROLL_PITCH_KI'
    RATEROLL_PITCH_KD = 'RATE_ROLL_PITCH_KD'

    RATE_YAW_KP = 'RATE_YAW_KP'
    RATE_YAW_KD = 'RATE_YAW_KD'

    TUNING_DISABLED = 0

    def __init__(self, amavlink):
        super(AMavlinkTune, self).__init__(amavlink)
        self._amavlink = amavlink
        self._tuning_parameters = {
            self.RATEROLL_PITCH_KP: {
                'tune_param_name': 'ATC_RAT_RLL_P',
                'tune_value': 4
            },
            self.RATEROLL_PITCH_KI: {
                'tune_param_name': 'ATC_RAT_RLL_I',
                'tune_value': 5
            },
            self.RATEROLL_PITCH_KD: {
                'tune_param_name': 'ATC_RAT_RLL_D',
                'tune_value': 21,
            },
            self.RATE_YAW_KP: {
                'tune_param_name': 'ATC_RAT_YAW_P',
                'tune_value': 6,
            },
            self.RATE_YAW_KD: {
                'tune_param_name': 'ATC_RAT_YAW_D',
                'tune_value': 26,
            },
        }
        self._actual_tuning_parameter = None
        self._original_value = None

    def disable(self):
        self._set_tune_param(0)
        self._actual_tuning_parameter = None
        self._original_value = None

    def get_actual_tune_param_value(self):
        if self._actual_tuning_parameter is None:
            return None
        else:
            return self._tuning_parameters[self._actual_tuning_parameter]['tune_value']

    def get_actual_tune_param_name(self):
        if self._actual_tuning_parameter is None:
            return None
        else:
            return self._tuning_parameters[self._actual_tuning_parameter]['tune_param_name']

    def get_actual_tune_value(self):
        return self._amavlink.param.get_value(self.get_actual_tune_param_name())

    def get_original_value(self):
        return self._original_value

    def get_tune_knob_pwm(self):
        return self._amavlink.rcinput.get_raw(channel=6)

    def get_tune_range(self):
        tune_low = self._amavlink.param.get_value(param_name='TUNE_LOW') / 1000.0
        tune_high = self._amavlink.param.get_value(param_name='TUNE_HIGH') / 1000.0
        return [tune_low, tune_high]

    def manual_tuning(self, tune_parameter):
        if self._amavlink.param.get_value(param_name='TUNE') != self.TUNING_DISABLED:
            self.disable()
            time.sleep(1)
        if not tune_parameter in self._tuning_parameters:
            raise AmavlinkUnknownTuneParameter(tune_parameter)
        self._actual_tuning_parameter = tune_parameter
        self._set_tune_limit(tune_param_name=self.get_actual_tune_param_name(), percent=20)
        self._set_tune_param(self.get_actual_tune_param_value())

    def _set_tune_param(self, tune_value):
        tune_value = int(tune_value)
        self._amavlink.param.set(param_name='TUNE', param_value=tune_value)
        # Using SITL the TUNE parameter has to be read several times until it is stable.
        for i in range(self.retries):
            if tune_value == int(self._amavlink.param.get_value(param_name='TUNE')):
                return
            time.sleep(self.retry_delay)
        raise AMavlinkTuneUnableToSetTuneKnob()

    def _set_tune_limit(self, tune_param_name, percent):
        self._original_value = self._amavlink.param.get_value(tune_param_name)
        self._amavlink.param.set('TUNE_LOW', self._tune_low_value(self._original_value, percent))
        self._amavlink.param.set('TUNE_HIGH', self._tune_high_value(self._original_value, percent))

    def _tune_low_value(self, actual_value, percent):
        limit = actual_value * (1.0 - float(percent) / 100.0)
        return self._convert_value_to_tune_limit(limit)

    def _tune_high_value(self, actual_value, percent):
        limit = actual_value * (1.0 + float(percent) / 100.0)
        return self._convert_value_to_tune_limit(limit)

    def _convert_value_to_tune_limit(self, value):
        return int(value * 1000.0)
