from ._connection import ConnectionControlInterface, ConnectionControl
from ._device import DeviceControlInterface, DeviceControl
from ._general import GeneralControlInterface, GeneralControl
from ._system import SystemCommand
from .data import Connection, Device, DeviceWifi, General

_syscmd = SystemCommand()
connection = ConnectionControl(_syscmd)
device = DeviceControl(_syscmd)
general = GeneralControl(_syscmd)
