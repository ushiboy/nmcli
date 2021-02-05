import re
from typing import List
from ._system import SystemCommandInterface, SystemCommand
from .data.device import Device, DeviceWifi, DeviceDetails
from .data.hotspot import Hotspot

class DeviceControlInterface:

    def __call__(self) -> List[Device]:
        raise NotImplementedError

    def status(self) -> List[Device]:
        raise NotImplementedError

    def show(self, ifname: str) -> DeviceDetails:
        raise NotImplementedError

    def show_all(self) -> List[DeviceDetails]:
        raise NotImplementedError

    def connect(self, ifname: str) -> None:
        raise NotImplementedError

    def disconnect(self, ifname: str) -> None:
        raise NotImplementedError

    def reapply(self, ifname: str) -> None:
        raise NotImplementedError

    def delete(self, ifname: str) -> None:
        raise NotImplementedError

    def wifi(self) -> List[DeviceWifi]:
        raise NotImplementedError

    def wifi_connect(self, ssid: str, password: str) -> None:
        raise NotImplementedError

    def wifi_hotspot(self,
                     ifname: str = None,
                     con_name: str = None,
                     ssid: str = None,
                     band: str = None,
                     channel: int = None,
                     password: str = None) -> Hotspot:
        raise NotImplementedError


class DeviceControl(DeviceControlInterface):

    def __init__(self, syscmd: SystemCommandInterface = None):
        self._syscmd = syscmd or SystemCommand()

    def __call__(self) -> List[Device]:
        return self.status()

    def status(self) -> List[Device]:
        r = self._syscmd.nmcli(['device', 'status'])
        results = []
        for row in r.split('\n')[1:]:
            if len(row) > 0:
                results.append(Device.parse(row))
        return results

    def show(self, ifname: str) -> DeviceDetails:
        r = self._syscmd.nmcli(['device', 'show', ifname])
        results = {}
        for row in r.split('\n'):
            m = re.search(r'^(\S+):\s*([\S\s]+)\s*', row)
            if m:
                key, value = m.groups()
                results[key] = None if value in ('--', '""') else value
        return results

    def show_all(self) -> List[DeviceDetails]:
        r = self._syscmd.nmcli(['device', 'show'])
        results = []
        details: DeviceDetails = {}
        for row in r.split('\n'):
            m = re.search(r'^(\S+):\s*([\S\s]+)\s*', row)
            if m:
                key, value = m.groups()
                if key == 'GENERAL.DEVICE':
                    details = {}
                    results.append(details)
                details[key] = None if value in ('--', '""') else value
        return results

    def connect(self, ifname: str) -> None:
        self._syscmd.nmcli(['device', 'connect', ifname])

    def disconnect(self, ifname: str) -> None:
        self._syscmd.nmcli(['device', 'disconnect', ifname])

    def reapply(self, ifname: str) -> None:
        self._syscmd.nmcli(['device', 'reapply', ifname])

    def delete(self, ifname: str) -> None:
        self._syscmd.nmcli(['device', 'delete', ifname])

    def wifi(self) -> List[DeviceWifi]:
        r = self._syscmd.nmcli(['-t', '-f', 'IN-USE,SSID,MODE,CHAN,RATE,SIGNAL,SECURITY',
            'device', 'wifi'])
        results = []
        rows = r.split('\n')
        for row in rows:
            if len(row) > 0:
                results.append(DeviceWifi.parse(row))
        return results

    def wifi_connect(self, ssid: str, password: str) -> None:
        self._syscmd.nmcli(['device', 'wifi', 'connect',
                            ssid, 'password', password])

    def wifi_hotspot(self,
                     ifname: str = None,
                     con_name: str = None,
                     ssid: str = None,
                     band: str = None,
                     channel: int = None,
                     password: str = None) -> Hotspot:
        raise NotImplementedError
