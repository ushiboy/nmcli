# pylint: disable=line-too-long
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, Optional

DeviceDetails = Dict[str, Optional[str]]


@dataclass(frozen=True)
class Device:
    device: str
    device_type: str
    state: str
    connection: Optional[str]

    def to_json(self):
        return {
            'device': self.device,
            'device_type': self.device_type,
            'state': self.state,
            'connection': self.connection
        }

    @classmethod
    def parse(cls, text: str) -> Device:
        m = re.search(r'^(\S*)\s+(\S*)\s+(\S*)\s+([\S\s]+)\s*$', text)
        if m:
            device, device_type, state, conn = m.groups()
            conn = conn.strip()
            connection = conn if conn != '--' else None
            return Device(device, device_type, state, connection)
        raise ValueError(f'Parse failed [{text}]')


@dataclass(frozen=True)
class DeviceWifi:
    in_use: bool
    ssid: str
    bssid: str
    mode: str
    chan: int
    freq: int
    rate: int
    signal: int
    security: str

    def to_json(self):
        return {
            'in_use': self.in_use,
            'ssid': self.ssid,
            'bssid': self.bssid,
            'mode': self.mode,
            'chan': self.chan,
            'freq': self.freq,
            'rate': self.rate,
            'signal': self.signal,
            'security': self.security
        }

    @classmethod
    def parse(cls, text: str) -> DeviceWifi:
        t = text.replace("\\:", "\uFFFE").replace(
            ":", "\uFFFF").replace("\uFFFE", ":")
        m = re.search(
            r'^(\*|\s)\uFFFF(.*)\uFFFF(.*)\uFFFF(.*)\uFFFF(\d+)\uFFFF(\d+)\sMHz\uFFFF(\d+)\sMbit\/s\uFFFF(\d+)\uFFFF(.*)$', t)
        if m:
            in_use, ssid, bssid, mode, chan, freq, rate, signal, security = m.groups()
            return DeviceWifi(in_use == '*', ssid, bssid, mode,
                              int(chan), int(freq), int(rate), int(signal), security.rstrip())
        raise ValueError(f'Parse failed [{text}]')
