from ._connection import ConnectionControl
from ._device import DeviceControl
from ._general import GeneralControl
from ._system import SystemCommand
from .data import Connection, Device, DeviceWifi, General

_syscmd = SystemCommand()
connection = ConnectionControl(_syscmd)
device = DeviceControl(_syscmd)
general = GeneralControl(_syscmd)
