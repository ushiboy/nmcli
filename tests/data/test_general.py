from nmcli._const import NetworkConnectivity
from nmcli.data import General

def test_to_json():
    state = 'connected'
    connectivity = NetworkConnectivity.FULL
    wifi_hw = True
    wifi = True
    wwan_hw = True
    wwan = True
    g = General(state, connectivity, wifi_hw, wifi, wwan_hw, wwan)
    assert g.to_json() == {
        'state':state,
        'connectivity':connectivity.value,
        'wifi_hw':wifi_hw,
        'wifi':wifi,
        'wwan_hw':wwan_hw,
        'wwan':wwan
    }
