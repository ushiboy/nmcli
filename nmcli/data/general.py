from dataclasses import dataclass

@dataclass(frozen=True)
class General:
    state: str
    connectivity: str
    wifi_hw: str
    wifi: str
    wwan_hw: str
    wwan: str
