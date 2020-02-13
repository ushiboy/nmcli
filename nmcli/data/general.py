from dataclasses import dataclass


@dataclass(frozen=True)
class General:
    state: str
    connectivity: str
    wifi_hw: str
    wifi: str
    wwan_hw: str
    wwan: str

    def to_json(self):
        return {
            'state': self.state,
            'connectivity': self.connectivity,
            'wifi_hw': self.wifi_hw,
            'wifi': self.wifi,
            'wwan_hw': self.wwan_hw,
            'wwan': self.wwan
        }
