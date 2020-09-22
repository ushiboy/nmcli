from __future__ import annotations
from dataclasses import dataclass
import re
from .._const import NetworkManagerState, NetworkConnectivity

@dataclass(frozen=True)
class General:
    state:NetworkManagerState
    connectivity: NetworkConnectivity
    wifi_hw: bool
    wifi: bool
    wwan_hw: bool
    wwan: bool

    def to_json(self):
        return {
            'state': self.state.value,
            'connectivity': self.connectivity.value,
            'wifi_hw': self.wifi_hw,
            'wifi': self.wifi,
            'wwan_hw': self.wwan_hw,
            'wwan': self.wwan
        }

    @classmethod
    def parse(cls, text: str) -> General:
        m = re.search(
            r'^([\S\s]+)\s{2}(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*', text)
        if m:
            state, connectivity, wifi_hw, wifi, wwan_hw, wwan = m.groups()
            return General(NetworkManagerState(state),
                           NetworkConnectivity(connectivity),
                           wifi_hw == 'enabled',
                           wifi == 'enabled',
                           wwan_hw == 'enabled',
                           wwan == 'enabled')
        raise ValueError('Parse failed [%s]' % text)
