import re
from typing import List, Tuple

from ._exception import ConnectionActivateFailedException
from ._helper import add_fields_option_if_needed, add_wait_option_if_needed
from ._system import SystemCommand, SystemCommandInterface
from .data.device import Device, DeviceDetails, DeviceWifi
from .data.hotspot import Hotspot


def parse_wifi_hotspot_result(text: str) -> Tuple[str, str, str]:
    m = re.search(r'Hotspot\spassword:\s(.*)', text)
    if m:
        password = m.groups()[0]
    m = re.search(
        r"Device\s'(.*)'\ssuccessfully\sactivated\swith\s'(.*)'", text)
    if m:
        ifname, uuid = m.groups()
    return (uuid, ifname, password)


def parse_hotspot_properties(text: str) -> Tuple[str, str]:
    for row in text.split('\n'):
        if len(row) == 0:
            continue
        m = re.search(r'^([\w\.\-]+):([\S\s]+)', row)
        if m is None:
            continue
        key, value = m.groups()
        if key == 'connection.id':
            con_name = value
        elif key == '802-11-wireless.ssid':
            ssid = value
    return (con_name, ssid)


class DeviceControlInterface:

    def __call__(self) -> List[Device]:
        raise NotImplementedError

    def status(self) -> List[Device]:
        raise NotImplementedError

    def show(self, ifname: str, fields: str = None) -> DeviceDetails:
        raise NotImplementedError

    def show_all(self, fields: str = None) -> List[DeviceDetails]:
        raise NotImplementedError

    def connect(self, ifname: str, wait: int = None) -> None:
        raise NotImplementedError

    def disconnect(self, ifname: str, wait: int = None) -> None:
        raise NotImplementedError

    def reapply(self, ifname: str) -> None:
        raise NotImplementedError

    def delete(self, ifname: str, wait: int = None) -> None:
        raise NotImplementedError

    def wifi(self, ifname: str = None, rescan: bool = None) -> List[DeviceWifi]:
        raise NotImplementedError

    def wifi_connect(self,
                     ssid: str,
                     password: str,
                     ifname: str = None,
                     wait: int = None) -> None:
        raise NotImplementedError

    def wifi_hotspot(self,
                     ifname: str = None,
                     con_name: str = None,
                     ssid: str = None,
                     band: str = None,
                     channel: int = None,
                     password: str = None) -> Hotspot:
        raise NotImplementedError

    def wifi_rescan(self,
                    ifname: str = None,
                    ssid: str = None) -> None:
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

    def show(self, ifname: str, fields: str = None) -> DeviceDetails:
        cmd = add_fields_option_if_needed(fields) + ['device', 'show', ifname]
        r = self._syscmd.nmcli(cmd)
        results = {}
        for row in r.split('\n'):
            m = re.search(r'^(\S+):\s*([\S\s]+)\s*', row)
            if m:
                key, value = m.groups()
                results[key] = None if value in ('--', '""') else value
        return results

    def show_all(self, fields: str = None) -> List[DeviceDetails]:
        cmd = add_fields_option_if_needed(fields) + ['device', 'show']
        r = self._syscmd.nmcli(cmd)
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

    def connect(self, ifname: str, wait: int = None) -> None:
        cmd = add_wait_option_if_needed(
            wait) + ['device', 'connect', ifname]
        self._syscmd.nmcli(cmd)

    def disconnect(self, ifname: str, wait: int = None) -> None:
        cmd = add_wait_option_if_needed(
            wait) + ['device', 'disconnect', ifname]
        self._syscmd.nmcli(cmd)

    def reapply(self, ifname: str) -> None:
        self._syscmd.nmcli(['device', 'reapply', ifname])

    def delete(self, ifname: str, wait: int = None) -> None:
        cmd = add_wait_option_if_needed(
            wait) + ['device', 'delete', ifname]
        self._syscmd.nmcli(cmd)

    def wifi(self, ifname: str = None, rescan: bool = None) -> List[DeviceWifi]:
        cmd = ['-t', '-f', 'IN-USE,SSID,BSSID,MODE,CHAN,FREQ,RATE,SIGNAL,SECURITY',
               'device', 'wifi', 'list']
        if ifname is not None:
            cmd += ['ifname', ifname]
        if rescan is not None:
            cmd += ['--rescan', 'yes' if rescan else 'no']
        r = self._syscmd.nmcli(cmd)
        results = []
        rows = r.split('\n')
        for row in rows:
            if len(row) > 0:
                results.append(DeviceWifi.parse(row))
        return results

    def wifi_connect(self,
                     ssid: str,
                     password: str,
                     ifname: str = None,
                     wait: int = None) -> None:
        cmd = add_wait_option_if_needed(
            wait) + ['device', 'wifi', 'connect', ssid, 'password', password]
        if ifname is not None:
            cmd += ['ifname', ifname]
        r = self._syscmd.nmcli(cmd)
        m = re.search(r'Connection activation failed:', r)
        if m:
            raise ConnectionActivateFailedException(
                'Connection activation failed')

    def wifi_hotspot(self,
                     ifname: str = None,
                     con_name: str = None,
                     ssid: str = None,
                     band: str = None,
                     channel: int = None,
                     password: str = None) -> Hotspot:
        cmd = ['device', 'wifi', 'hotspot', '--show-secrets']
        if ifname is not None:
            cmd += ['ifname', ifname]
        if con_name is not None:
            cmd += ['con-name', con_name]
        if ssid is not None:
            cmd += ['ssid', ssid]
        if band is not None:
            cmd += ['band', band]
        if channel is not None:
            cmd += ['channel', str(channel)]
        if password is not None:
            cmd += ['password', password]
        r = self._syscmd.nmcli(cmd)
        uuid, ifname, password = parse_wifi_hotspot_result(r)
        r = self._syscmd.nmcli(['-t', '-f', 'connection.id,802-11-wireless.ssid',
                                'connection', 'show', 'uuid', uuid])
        con_name, ssid = parse_hotspot_properties(r)
        return Hotspot(ifname, con_name, ssid, password)

    def wifi_rescan(self,
                    ifname: str = None,
                    ssid: str = None) -> None:
        cmd = ['device', 'wifi', 'rescan']
        if ifname is not None:
            cmd += ['ifname', ifname]
        if ssid is not None:
            cmd += ['ssid', ssid]
        self._syscmd.nmcli(cmd)
