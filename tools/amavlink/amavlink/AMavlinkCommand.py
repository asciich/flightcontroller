from AMavlinkErrors import ErrorAMavlinkNoCommandSpecified, ErrorAMavCommandACKNotReceived


class AMavlinkCommand():

    def __init__(self, amavlink):
        self._amavlink = amavlink

    def send_long(self, autopilot_system_id=None, autopilot_component_id=None, command_id=None, cofirmation=1,
                  param1=0,
                  param2=0,
                  param3=0,
                  param4=0,
                  param5=0,
                  param6=0,
                  param7=0
                  ):
        self._amavlink.heartbeat.wait_if_target_unknown()
        if command_id is None:
            raise ErrorAMavlinkNoCommandSpecified()
        if autopilot_component_id is None:
            autopilot_component_id = self._amavlink.heartbeat.component_id
        if autopilot_system_id is None:
            autopilot_system_id = self._amavlink.heartbeat.system_id
        mavutil = self._amavlink.get_mavutil()
        mavutil.mav.command_long_send(
            autopilot_system_id,
            autopilot_component_id,
            command=command_id,
            confirmation=cofirmation,
            param1=param1,
            param2=param2,
            param3=param3,
            param4=param4,
            param5=param5,
            param6=param6,
            param7=param7
        )

    def arm(self):
        self.send_long(command_id=400, param1=1)  # TODO use enum for command id
        mavutil = self._amavlink.get_mavutil()
        ack_message = mavutil.recv_match('ACTION_ACK', blocking=True, timeout=10)
        if ack_message is None:
            raise ErrorAMavCommandACKNotReceived()

    def disarm(self):
        self.send_long(command_id=400, param1=0)  # TODO use enum for command id

    def preflight_storage_read_params_from_flash(self):
        self.send_long(command_id=245, param1=1)
