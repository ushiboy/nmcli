from ._connection import ConnectionControl, ConnectionControlInterface
from ._const import NetworkConnectivity, NetworkManagerState
from ._device import DeviceControl, DeviceControlInterface
from ._exception import (ConnectionActivateFailedException,
                         ConnectionDeactivateFailedException,
                         ConnectionDeleteFailedException,
                         DisconnectDeviceFailedException,
                         InvalidUserInputException,
                         NetworkManagerNotRunningException, NotExistException,
                         ScanningNotAllowedException, TimeoutExpiredException,
                         UnspecifiedException)
from ._general import GeneralControl, GeneralControlInterface
from ._networking import NetworkingControl, NetworkingControlInterface
from ._radio import RadioControl, RadioControlInterface
from ._system import CommandParameter, SystemCommand, SystemCommandInterface
from .data import (Connection, ConnectionDetails, ConnectionOptions, Device,
                   DeviceDetails, DeviceWifi, General, Radio)

_syscmd = SystemCommand()
connection = ConnectionControl(_syscmd)
device = DeviceControl(_syscmd)
general = GeneralControl(_syscmd)
networking = NetworkingControl(_syscmd)
radio = RadioControl(_syscmd)

def disable_use_sudo():
    _syscmd.disable_use_sudo()
