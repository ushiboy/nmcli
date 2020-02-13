from dataclasses import dataclass
from typing import Optional


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
