from nmcli.data import Hotspot

def test_to_json():
    ifname = 'eth0'
    con_name = 'con'
    ssid = 'abcdef'
    band = 'a'
    channel = 123
    password = 'pass'
    h = Hotspot(ifname, con_name, ssid, band, channel, password)
    assert h.to_json() == {
        'ifname': ifname,
        'con_name': con_name,
        'ssid': ssid,
        'band': band,
        'channel': channel,
        'password': password
    }
