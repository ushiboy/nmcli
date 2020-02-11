from ._connection import ConnectionControl
from ._device import DeviceControl
from ._general import GeneralControl
from ._system import SystemCommand

_syscmd = SystemCommand()
connection = ConnectionControl(_syscmd)
device = DeviceControl(_syscmd)
general = GeneralControl(_syscmd)
