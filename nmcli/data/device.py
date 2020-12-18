from __future__ import annotations
from dataclasses import dataclass
import re
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
        raise ValueError('Parse failed [%s]' % text)


@dataclass(frozen=True)
class DeviceWifi:
    in_use: bool
    ssid: str
    mode: str
    chan: int
    rate: int
    signal: int
    security: str

    def to_json(self):
        return {
            'in_use': self.in_use,
            'ssid': self.ssid,
            'mode': self.mode,
            'chan': self.chan,
            'rate': self.rate,
            'signal': self.signal,
            'security': self.security
        }

    @classmethod
    def parse(cls, text: str) -> DeviceWifi:
        m = re.search(
            r'^(\*|\s)\s+(\S*)\s+(\S*)\s+(\d+)\s+(\d+)\sMbit/s\s+(\d+)\s+\S+\s+(.*)$', text)
        if m:
            in_use, ssid, mode, chan, rate, signal, security = m.groups()
            return DeviceWifi(in_use == '*', ssid, mode,
                    int(chan), int(rate), int(signal), security.rstrip())
        raise ValueError('Parse failed [%s]' % text)
