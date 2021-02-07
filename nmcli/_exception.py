class UnspecifiedException(Exception):
    """
    1 Unknown or unspecified error.
    """


class InvalidUserInputException(Exception):
    """
    2 Invalid user input, wrong nmcli invocation.
    """


class TimeoutExpiredException(Exception):
    """
    3 Timeout expired.
    """


class ConnectionActivateFailedException(Exception):
    """
    4 Connection activation failed.
    """


class ConnectionDeactivateFailedException(Exception):
    """
    5 Connection deactivation failed.
    """


class DisconnectDeviceFailedException(Exception):
    """
    6 Disconnecting device failed.
    """


class ConnectionDeleteFailedException(Exception):
    """
    7 Connection deletion failed.
    """


class NetworkManagerNotRunningException(Exception):
    """
    8 NetworkManager is not running.
    """


class NotExistException(Exception):
    """
    10 Connection, device, or access point does not exist.
    """


class ScanningNotAllowedException(Exception):
    """
    Scanning not allowed.
    """
