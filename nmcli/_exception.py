class UnspecifiedException(Exception):
    """
    1 Unknown or unspecified error.
    """
    pass

class InvalidUserInputException(Exception):
    """
    2 Invalid user input, wrong nmcli invocation.
    """
    pass

class TimeoutExpiredException(Exception):
    """
    3 Timeout expired.
    """
    pass

class ConnectionActivateFailedException(Exception):
    """
    4 Connection activation failed.
    """
    pass

class ConnectionDeactivateFailedException(Exception):
    """
    5 Connection deactivation failed.
    """
    pass

class DisconnectDeviceFailedException(Exception):
    """
    6 Disconnecting device failed.
    """
    pass

class ConnectionDeleteFailedException(Exception):
    """
    7 Connection deletion failed.
    """
    pass

class NetworkManagerNotRunningException(Exception):
    """
    8 NetworkManager is not running.
    """
    pass

class NotExistException(Exception):
    """
    10 Connection, device, or access point does not exist.
    """
    pass
