# pylint: disable=line-too-long
from nmcli.data import Device, DeviceWifi

def test_device_to_json():
    device = 'eth0'
    device_type = 'ethernet'
    state = 'connected'
    connection = 'Home'
    d = Device(device, device_type, state, connection)
    assert d.to_json() == {
        'device':device,
        'device_type':device_type,
        'state':state,
        'connection':connection
    }

def test_device_wifi_to_json():
    in_use = True
    ssid = 'AP1'
    mode = 'Infra'
    chan = 1
    rate = 130
    signal = 10
    security = 'WPA1'
    d = DeviceWifi(in_use, ssid, mode, chan, rate, signal, security)
    assert d.to_json() == {
        'in_use': in_use,
        'ssid': ssid,
        'mode': mode,
        'chan': chan,
        'rate': rate,
        'signal': signal,
        'security': security
    }

def test_device_wifi_parse():
    d1 = '*       AP1  Infra  1     130 Mbit/s  82      ______  WPA1 WPA2'
    assert DeviceWifi.parse(d1) == \
        DeviceWifi(True, 'AP1', 'Infra', 1, 130, 82, 'WPA1 WPA2')
    d2 = '        AP1  Infra  1     130 Mbit/s  82      ______  WPA1 WPA2'
    assert DeviceWifi.parse(d2) == \
        DeviceWifi(False, 'AP1', 'Infra', 1, 130, 82, 'WPA1 WPA2')
    d3 = '        AP 1  Infra  1     130 Mbit/s  82      ______  WPA1 WPA2'
    assert DeviceWifi.parse(d3) == \
        DeviceWifi(False, 'AP 1', 'Infra', 1, 130, 82, 'WPA1 WPA2')
    d4 = '        AP 1 2  Infra  1     130 Mbit/s  82      ______  WPA1 WPA2'
    assert DeviceWifi.parse(d4) == \
        DeviceWifi(False, 'AP 1 2', 'Infra', 1, 130, 82, 'WPA1 WPA2')

def test_device_wifi_parse_include_bssid_line():
    d1 = '*       00:00:00:00:00:00  AP1  Infra  1     130 Mbit/s  82      ______  WPA1 WPA2'
    assert DeviceWifi.parse_include_bssid_line(d1) == \
        DeviceWifi(True, 'AP1', 'Infra', 1, 130, 82, 'WPA1 WPA2')
    d2 = '        00:00:00:00:00:00  AP1  Infra  1     130 Mbit/s  82      ______  WPA1 WPA2'
    assert DeviceWifi.parse_include_bssid_line(d2) == \
        DeviceWifi(False, 'AP1', 'Infra', 1, 130, 82, 'WPA1 WPA2')
    d3 = '        00:00:00:00:00:00  AP 2  Infra  1     130 Mbit/s  82      ______  WPA1 WPA2'
    assert DeviceWifi.parse_include_bssid_line(d3) == \
        DeviceWifi(False, 'AP 2', 'Infra', 1, 130, 82, 'WPA1 WPA2')
    d4 = '        00:00:00:00:00:00  AP 3 1  Infra  1     130 Mbit/s  82      ______  WPA1 WPA2'
    assert DeviceWifi.parse_include_bssid_line(d4) == \
        DeviceWifi(False, 'AP 3 1', 'Infra', 1, 130, 82, 'WPA1 WPA2')
    d5 = '        00:00:00:00:00:00  AAAAAA-BB-CC DDDDDDDDD EEE 9999  Infra  11     65 Mbit/s  49      ______  WPA2'
    assert DeviceWifi.parse_include_bssid_line(d5) == \
        DeviceWifi(False, 'AAAAAA-BB-CC DDDDDDDDD EEE 9999', 'Infra', 11, 65, 49, 'WPA2')
