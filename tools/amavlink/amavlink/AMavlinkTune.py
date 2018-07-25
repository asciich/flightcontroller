import time

from AMavlinkDefaultObject import AMavlinkDefaultObject
from AMavlinkErrors import AMavlinkTuneUnableToSetTuneKnob


class AMavlinkTune(AMavlinkDefaultObject):
    RATEROLL_PITCHKP = 'RATEROLL_PITCHKP'

    def __init__(self, amavlink):
        super(AMavlinkTune, self).__init__(amavlink)
        self._amavlink = amavlink
        self._tuning_parameters = {
            self.RATEROLL_PITCHKP: {
                'modify_param_name': 'ATC_RAT_RLL_P'
            }
        }

    def disable(self):
        self._set_tune_param(0)

    def manual_tuning(self, tune_parameter):
        self._set_tune_limit(modify_param_name='ATC_RAT_RLL_P', percent=20)
        self._set_tune_param(4)

    def _set_tune_param(self, tune_value):
        tune_value = int(tune_value)
        self._amavlink.param.set(param_name='TUNE', param_value=tune_value)
        # Using SITL the TUNE parameter has to be read several times until it is stable.
        for i in range(self.retries):
            if tune_value == int(self._amavlink.param.get_value(param_name='TUNE')):
                return
            time.sleep(self.retry_delay)
        raise AMavlinkTuneUnableToSetTuneKnob()

    def _set_tune_limit(self, modify_param_name, percent):
        actual_value = self._amavlink.param.get_value(modify_param_name)
        self._amavlink.param.set('TUNE_LOW', self._tune_low_value(actual_value, percent))
        self._amavlink.param.set('TUNE_HIGH', self._tune_high_value(actual_value, percent))

    def _tune_low_value(self, actual_value, percent):
        limit = actual_value * (1.0 - float(percent) / 100.0)
        return self._convert_value_to_tune_limit(limit)

    def _tune_high_value(self, actual_value, percent):
        limit = actual_value * (1.0 + float(percent) / 100.0)
        return self._convert_value_to_tune_limit(limit)

    def _convert_value_to_tune_limit(self, value):
        return int(value * 1000.0)
