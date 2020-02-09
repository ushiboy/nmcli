from ._device import DeviceControl
from ._system import SystemCommand

_syscmd = SystemCommand()
device = DeviceControl(_syscmd)
