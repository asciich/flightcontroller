import time

from AMavlinkDefaultObject import AMavlinkDefaultObject
from AMavlinkErrors import AMavlinkRCChannelInvalid, AMavLinkError, AMavlinkRCOverrideError


class AMavlinkRCInput(AMavlinkDefaultObject):

    def __init__(self, amavlink):
        super(AMavlinkRCInput, self).__init__(amavlink)
        self._amavlink = amavlink

    def deactivate_override(self):
        channel_values = [0] * 8
        self._send_channel_values(channel_values)

    def override(self, channel, pwm_value):
        self.logger.debug('Override channel {} with pwm value {} requested'.format(channel, pwm_value))
        self._check_channel_valid(channel)
        channel = int(channel)
        pwm_value = int(pwm_value)

        channel_values = [0] * 8
        channel_values[channel - 1] = pwm_value

        self._send_channel_values(channel_values)

        for i in range(self.retries):
            if pwm_value == self.get_raw(channel):
                self.logger.info('RC channel {} override to {}'.format(channel, pwm_value))
                return
            time.sleep(0.5)
        self.logger.error('Unable to override channel {} with pwm value {}'.format(channel, pwm_value))
        raise AMavlinkRCOverrideError()

    def get_raw(self, channel):
        self._check_channel_valid(channel)
        self._amavlink.param.send_request_for_param('RC_CHANNELS_RAW')
        channel_message = self._amavlink.message.get(strmatch='RC_CHANNELS_RAW', blocking=True)
        self.logger.debug('Channel message to get_raw value of channel {}: "{}"'.format(channel, channel_message))

        if channel == 1:
            return channel_message.chan1_raw
        elif channel == 2:
            return channel_message.chan2_raw
        elif channel == 3:
            return channel_message.chan3_raw
        elif channel == 4:
            return channel_message.chan4_raw
        elif channel == 5:
            return channel_message.chan5_raw
        elif channel == 6:
            return channel_message.chan6_raw
        elif channel == 7:
            return channel_message.chan7_raw
        elif channel == 8:
            return channel_message.chan8_raw

        error_msg = 'Unknown state in AMAvlinkRCInput.get_raw'
        self.logger.error(error_msg)
        raise AMavLinkError(error_msg)

    def _check_channel_valid(self, channel):
        if channel <= 0 or channel > 8:
            raise AMavlinkRCChannelInvalid('{} is not a valid channel number (1-8)'.format(channel))
        return True

    def _send_channel_values(self, channel_values):
        self._amavlink.heartbeat.wait_if_target_unknown()
        mavutil = self._amavlink.get_mavutil()
        mavutil.mav.rc_channels_override_send(self._amavlink.heartbeat.system_id, self._amavlink.heartbeat.component_id,
                                              *channel_values)
