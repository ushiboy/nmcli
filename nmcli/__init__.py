from ._connection import ConnectionControlInterface, ConnectionControl
from ._const import NetworkConnectivity
from ._device import DeviceControlInterface, DeviceControl
from ._exception import UnspecifiedException, \
    InvalidUserInputException, \
    TimeoutExpiredException, \
    ConnectionActivateFailedException, \
    ConnectionDeactivateFailedException, \
    DisconnectDeviceFailedException, \
    ConnectionDeleteFailedException, \
    NetworkManagerNotRunningException, \
    NotExistException
from ._general import GeneralControlInterface, GeneralControl
from ._networking import NetworkingControlInterface, NetworkingControl
from ._radio import RadioControlInterface, RadioControl
from ._system import SystemCommand
from .data import Connection, Device, DeviceWifi, General, Radio

_syscmd = SystemCommand()
connection = ConnectionControl(_syscmd)
device = DeviceControl(_syscmd)
general = GeneralControl(_syscmd)
networking = NetworkingControl(_syscmd)
radio = RadioControl(_syscmd)
