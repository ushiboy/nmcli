from nmcli._const import NetworkConnectivity, NetworkManagerState
from nmcli.data import General


def test_to_json():
    state = NetworkManagerState.CONNECTED_GLOBAL
    connectivity = NetworkConnectivity.FULL
    wifi_hw = True
    wifi = True
    wwan_hw = True
    wwan = True
    g = General(state, connectivity, wifi_hw, wifi, wwan_hw, wwan)
    assert g.to_json() == {
        'state':state.value,
        'connectivity':connectivity.value,
        'wifi_hw':wifi_hw,
        'wifi':wifi,
        'wwan_hw':wwan_hw,
        'wwan':wwan
    }

def test_parse():
    d1 = 'unknown  none          enabled  enabled  enabled  disabled'
    assert General.parse(d1) == General(NetworkManagerState.UNKNOWN,
                                        NetworkConnectivity.NONE,
                                        True, True, True, False)

    d2 = 'asleep  portal          enabled  enabled  disabled  enabled'
    assert General.parse(d2) == General(NetworkManagerState.ASLEEP,
                                        NetworkConnectivity.PORTAL,
                                        True, True, False, True)

    d3 = 'connecting  limited          enabled  disabled  enabled  enabled'
    assert General.parse(d3) == General(NetworkManagerState.CONNECTING,
                                        NetworkConnectivity.LIMITED,
                                        True, False, True, True)

    d4 = 'connected (local only)  full          disabled  enabled  enabled  enabled'
    assert General.parse(d4) == General(NetworkManagerState.CONNECTED_LOCAL,
                                        NetworkConnectivity.FULL,
                                        False, True, True, True)

    d5 = 'connected (site only)  full          enabled  enabled  enabled  enabled'
    assert General.parse(d5) == General(NetworkManagerState.CONNECTED_SITE,
                                        NetworkConnectivity.FULL,
                                        True, True, True, True)

    d6 = 'disconnecting  full          enabled  enabled  enabled  enabled'
    assert General.parse(d6) == General(NetworkManagerState.DISCONNECTING,
                                        NetworkConnectivity.FULL,
                                        True, True, True, True)

    d7 = 'disconnected  full          enabled  enabled  enabled  enabled'
    assert General.parse(d7) == General(NetworkManagerState.DISCONNECTED,
                                        NetworkConnectivity.FULL,
                                        True, True, True, True)
