from nmcli.data import General

def test_to_json():
    state = 'connected'
    connectivity = 'full'
    wifi_hw = 'enabled'
    wifi = 'enabled'
    wwan_hw = 'enabled'
    wwan = 'enabled'
    g = General(state, connectivity, wifi_hw, wifi, wwan_hw, wwan)
    assert g.to_json() == {
        'state':state,
        'connectivity':connectivity,
        'wifi_hw':wifi_hw,
        'wifi':wifi,
        'wwan_hw':wwan_hw,
        'wwan':wwan
    }
