from nmcli.data import Radio


def test_to_json():
    wifi_hw = True
    wifi = True
    wwan_hw = True
    wwan = True
    r = Radio(wifi_hw, wifi, wwan_hw, wwan)
    assert r.to_json() == {
        'wifi_hw':wifi_hw,
        'wifi':wifi,
        'wwan_hw':wwan_hw,
        'wwan':wwan
    }
