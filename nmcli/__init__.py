from ._connection import ConnectionControlInterface, ConnectionControl
from ._const import NetworkManagerState, NetworkConnectivity
from ._device import DeviceControlInterface, DeviceControl
from ._exception import UnspecifiedException, \
    InvalidUserInputException, \
    TimeoutExpiredException, \
    ConnectionActivateFailedException, \
    ConnectionDeactivateFailedException, \
    DisconnectDeviceFailedException, \
    ConnectionDeleteFailedException, \
    NetworkManagerNotRunningException, \
    NotExistException, \
    ScanningNotAllowedException
from ._general import GeneralControlInterface, GeneralControl
from ._networking import NetworkingControlInterface, NetworkingControl
from ._radio import RadioControlInterface, RadioControl
from ._system import SystemCommand, SystemCommandInterface, CommandParameter
from .data import Connection, \
        ConnectionDetails, \
        ConnectionOptions, \
        Device, \
        DeviceWifi, \
        DeviceDetails, \
        General, \
        Radio

_syscmd = SystemCommand()
connection = ConnectionControl(_syscmd)
device = DeviceControl(_syscmd)
general = GeneralControl(_syscmd)
networking = NetworkingControl(_syscmd)
radio = RadioControl(_syscmd)

def disable_use_sudo():
    _syscmd.disable_use_sudo()
