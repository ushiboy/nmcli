from __future__ import annotations

import re
from dataclasses import dataclass

from .._const import NetworkConnectivity, NetworkManagerState


@dataclass(frozen=True)
class General:
    state: NetworkManagerState
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

# case 1:
# STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN     METERED
# connected  full          enabled  enabled  missing  enabled  no (guessed)
#
# case 2:
# unknown  none          enabled  enabled  enabled  disabled
#
# case 3:
# connected (local only)  full          disabled  enabled  enabled  enabled
#
# see: https://regex101.com/r/zW1hHE/1

    @classmethod
    def parse(cls, text: str) -> General:
        pattern = (
            r'^'
            + r'(?P<state>.+)'
            + r'  '
            + r'(?P<connectivity>\S+)'
            + r'\s+'
            + r'(?P<wifi_hw>\S+)'
            + r'  '
            + r'(?P<wifi>\S+)'
            + r'  '
            + r'(?P<wwan_hw>\S+)'
            + r'  '
            + r'(?P<wwan>\S+)'
            + r'(?:  (?P<metered>.+)?)?'
            + r'$'
        )

        # The execution result will have a trailing space, so trim it and then match it to the pattern.
        m = re.search(pattern, text.rstrip())

        if m:
            state, connectivity, wifi_hw, wifi, wwan_hw, wwan, _metered = m.groups()
            return General(NetworkManagerState(state),
                           NetworkConnectivity(connectivity),
                           wifi_hw == 'enabled',
                           wifi == 'enabled',
                           wwan_hw == 'enabled',
                           wwan == 'enabled')
        raise ValueError(f'Parse failed [{text}]')
