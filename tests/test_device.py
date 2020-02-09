from .helper import DummySystemCommand
from nmcli._device import DeviceControl
from nmcli.data import Device, DeviceWifi
import pytest

def test_device():
    s = DummySystemCommand('''DEVICE  TYPE      STATE      CONNECTION
eth0    ethernet  connected  Default
wlan0   wifi      connected  MyWifi
lo      loopback  unmanaged  --''')
    device = DeviceControl(s)
    r = device()
    assert len(r) == 3
    assert r == [
        Device('eth0', 'ethernet', 'connected', 'Default'),
        Device('wlan0', 'wifi', 'connected', 'MyWifi'),
        Device('lo', 'loopback', 'unmanaged', None)
    ]
    assert s.passed_parameters == 'device'

def test_device_wifi():
    s = DummySystemCommand('''IN-USE  SSID             MODE   CHAN  RATE        SIGNAL  BARS  SECURITY
*       AP1  Infra  1     130 Mbit/s  82      ______  WPA1 WPA2
        AP2  Infra  11    195 Mbit/s  74      ______  WPA2
        AP3  Infra  11    195 Mbit/s  72      ______  WPA1 WPA2''')
    device = DeviceControl(s)
    r = device.wifi()
    assert len(r) == 3
    assert r == [
        DeviceWifi(True, 'AP1', 'Infra', 1, 130, 82, 'WPA1 WPA2'),
        DeviceWifi(False, 'AP2', 'Infra', 11, 195, 74, 'WPA2'),
        DeviceWifi(False, 'AP3', 'Infra', 11, 195, 72, 'WPA1 WPA2'),
    ]
    assert s.passed_parameters == ['device', 'wifi']

def test_wifi_connect():
    s = DummySystemCommand()
    device = DeviceControl(s)
    ssid = 'AP1'
    password = 'abc'
    device.wifi_connect(ssid, password)
    assert s.passed_parameters == ['device', 'wifi', 'connect', ssid, 'password', password]
