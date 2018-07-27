class AMavLinkError(Exception):
    pass


class ErrorAMavlinkNotConnected(AMavLinkError):
    pass


class ErrorAMavlinkNoCommandSpecified(AMavLinkError):
    pass


class ErrorAMavCommandACKNotReceived(AMavLinkError):
    pass


class AMavlinkParamNotReceiveError(AMavLinkError):
    pass


class AMavlinkMessageNotReceivedError(AMavLinkError):
    pass


class AMavlinkBootNotFinishedError(AMavLinkError):
    pass


class AMavlinkParamVerificationError(AMavLinkError):
    pass


class AMavlinkParamSetError(AMavLinkError):
    pass


class AMavlinkHeartbeatNotReceivedError(AMavLinkError):
    pass


class AMavlinkCLIParseError(AMavLinkError):
    pass


class AMavlinkCLIParamVerificationError(AMavLinkError):
    pass


class AMavlinkParamFileDelimiterNotFoundInLineError(AMavLinkError):
    pass


class AMavlinkParamFileWriteEmptyFileError(AMavLinkError):
    pass


class AMavlinClearRecvBufferError(AMavLinkError):
    pass


class AMavlinkTuneUnableToSetTuneKnob(AMavLinkError):
    pass


class AMavlinkRCChannelInvalid(AMavLinkError):
    pass


class AMavlinkRCOverrideError(AMavLinkError):
    pass


class AmavlinkUnknownTuneParameter(AMavLinkError):
    pass
