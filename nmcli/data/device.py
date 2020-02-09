from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Device:
    device: str
    device_type: str
    state: str
    connection: Optional[str]

@dataclass(frozen=True)
class DeviceWifi:
    in_use: bool
    ssid: str
    mode: str
    chan: int
    rate: int
    signal: int
    security: str
