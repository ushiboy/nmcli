import pytest
from nmcli.dummy._device import DummyDeviceControl
from nmcli.data import Device, DeviceWifi

def test_call():
    result_call = [Device('eth0', 'ethernet', 'connected,', 'MyNet')]
    c = DummyDeviceControl(result_call)
    assert c() == result_call

def test_call_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    with pytest.raises(Exception):
        c()

def test_wifi():
    result_wifi = [DeviceWifi(False, 'ssid', 'Infra', 1, 54, 78, 'WPA2')]
    c = DummyDeviceControl(result_wifi=result_wifi)
    assert c.wifi() == result_wifi

def test_wifi_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.wifi()

def test_wifi_connect():
    c = DummyDeviceControl()
    ssid = 'ssid'
    password = 'passwd'
    c.wifi_connect(ssid, password)
    assert c.wifi_connect_args == [(ssid, password)]

def test_wifi_connect_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    ssid = 'ssid'
    password = 'passwd'
    with pytest.raises(Exception):
        c.wifi_connect(ssid, password)
