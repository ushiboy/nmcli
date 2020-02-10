from ._system import SystemCommandInterface, SystemCommand
from .data.device import Device, DeviceWifi
from typing import List, Optional
import re

class DeviceControlInterface:

    def __call__(self) -> List[Device]:
        raise NotImplementedError

    def wifi(self) -> List[DeviceWifi]:
        raise NotImplementedError

    def wifi_connect(self, ssid: str, password: str) -> None:
        raise NotImplementedError

class DeviceControl(DeviceControlInterface):

    def __init__(self, syscmd: SystemCommandInterface=None):
        self._syscmd = syscmd or SystemCommand()

    def __call__(self) -> List[Device]:
        r = self._syscmd.nmcli('device')
        results = []
        for row in r.split('\n')[1:]:
            m = re.search(r'^(\S*)\s+(\S*)\s+(\S*)\s+(\S*)\s*$', row)
            if m:
                device, device_type, state, conn = m.groups()
                connection = conn if conn != '--' else None
                results.append(Device(device, device_type, state, connection))
        return results

    def wifi(self) -> List[DeviceWifi]:
        r = self._syscmd.nmcli(['device', 'wifi'])
        results = []
        for row in r.split('\n')[1:]:
            m = re.search(r'^(\*|\s)\s+(\S*)\s+(\S*)\s+(\d+)\s+(\d+)\sMbit/s\s+(\d+)\s+\S+\s+(.*)$', row)
            if m:
                in_use, ssid, mode, chan, rate, signal, security = m.groups()
                results.append(DeviceWifi(in_use == '*', ssid, mode,
                    int(chan), int(rate), int(signal), security.rstrip()))
        return results

    def wifi_connect(self, ssid: str, password: str) -> None:
        self._syscmd.nmcli(['device', 'wifi', 'connect', ssid, 'password', password])
