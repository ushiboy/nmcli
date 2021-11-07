# pylint: disable=line-too-long
import pytest

from nmcli.data import Device, DeviceWifi


def test_device_to_json():
    device = 'eth0'
    device_type = 'ethernet'
    state = 'connected'
    connection = 'Home'
    d = Device(device, device_type, state, connection)
    assert d.to_json() == {
        'device': device,
        'device_type': device_type,
        'state': state,
        'connection': connection
    }


def test_device_parse():
    d1 = 'eth0    ethernet  connected  Default'
    assert Device.parse(d1) == \
        Device('eth0', 'ethernet', 'connected', 'Default')
    d2 = 'lo      loopback  unmanaged  --'
    assert Device.parse(d2) == \
        Device('lo', 'loopback', 'unmanaged', None)


def test_device_parse_when_failed():
    with pytest.raises(ValueError) as e:
        Device.parse('invalid')
    assert str(e.value) == 'Parse failed [invalid]'


def test_device_wifi_to_json():
    in_use = True
    ssid = 'AP1'
    bssid = '00:00:00:00:00:00'
    mode = 'Infra'
    chan = 1
    freq = 2400
    rate = 130
    signal = 10
    security = 'WPA1'
    d = DeviceWifi(in_use, ssid, bssid, mode, chan, freq, rate, signal, security)
    assert d.to_json() == {
        'in_use': in_use,
        'ssid': ssid,
        'bssid': bssid,
        'mode': mode,
        'chan': chan,
        'freq': freq,
        'rate': rate,
        'signal': signal,
        'security': security
    }


def test_device_wifi_parse():
    d1 = '*:AP1:00\\:00\\:00\\:00\\:00\\:00:Infra:1:2400 MHz:130 Mbit/s:82:WPA1 WPA2'
    assert DeviceWifi.parse(d1) == \
            DeviceWifi(True, 'AP1', '00:00:00:00:00:00', 'Infra', 1, 2400, 130, 82, 'WPA1 WPA2')
    d2 = ' :AP1:00\\:00\\:00\\:00\\:00\\:01:Infra:1:2401 MHz:130 Mbit/s:82:WPA1 WPA2'
    assert DeviceWifi.parse(d2) == \
        DeviceWifi(False, 'AP1', '00:00:00:00:00:01', 'Infra', 1, 2401, 130, 82, 'WPA1 WPA2')
    d3 = ' :AP 1:00\\:00\\:00\\:00\\:00\\:02:Infra:1:2402 MHz:130 Mbit/s:82:WPA1 WPA2'
    assert DeviceWifi.parse(d3) == \
        DeviceWifi(False, 'AP 1', '00:00:00:00:00:02', 'Infra', 1, 2402, 130, 82, 'WPA1 WPA2')
    d4 = ' :AAAAAA BBBBBBBBB CCC 9999:00\\:00\\:00\\:00\\:00\\:03:Infra:1:2403 MHz:130 Mbit/s:82:WPA1 WPA2'
    assert DeviceWifi.parse(d4) == \
        DeviceWifi(False, 'AAAAAA BBBBBBBBB CCC 9999', '00:00:00:00:00:03',
                   'Infra', 1, 2403, 130, 82, 'WPA1 WPA2')

def test_device_wifi_parse_when_failed():
    d = '*:AP1:Infra:1:130 Mbit/s:82:WPA1 WPA2'
    with pytest.raises(ValueError) as e:
        DeviceWifi.parse(d)
    assert str(e.value) == 'Parse failed [%s]' % d
