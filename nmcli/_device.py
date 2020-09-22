from typing import List
from ._system import SystemCommandInterface, SystemCommand
from .data.device import Device, DeviceWifi


class DeviceControlInterface:

    def __call__(self) -> List[Device]:
        raise NotImplementedError

    def wifi(self) -> List[DeviceWifi]:
        raise NotImplementedError

    def wifi_connect(self, ssid: str, password: str) -> None:
        raise NotImplementedError


class DeviceControl(DeviceControlInterface):

    def __init__(self, syscmd: SystemCommandInterface = None):
        self._syscmd = syscmd or SystemCommand()

    def __call__(self) -> List[Device]:
        r = self._syscmd.nmcli('device')
        results = []
        for row in r.split('\n')[1:]:
            results.append(Device.parse(row))
        return results

    def wifi(self) -> List[DeviceWifi]:
        r = self._syscmd.nmcli(['device', 'wifi'])
        results = []
        for row in r.split('\n')[1:]:
            results.append(DeviceWifi.parse(row))
        return results

    def wifi_connect(self, ssid: str, password: str) -> None:
        self._syscmd.nmcli(['device', 'wifi', 'connect',
                            ssid, 'password', password])
