import pytest

from nmcli.data import Device, DeviceWifi, Hotspot
from nmcli.dummy._device import DummyDeviceControl


def test_call():
    result_call = [Device('eth0', 'ethernet', 'connected,', 'MyNet')]
    c = DummyDeviceControl(result_call)
    assert c() == result_call


def test_call_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    with pytest.raises(Exception):
        c()


def test_status():
    result_call = [Device('eth0', 'ethernet', 'connected,', 'MyNet')]
    c = DummyDeviceControl(result_call)
    assert c.status() == result_call


def test_status_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.status()


def test_show():
    result_show = {'key': 'value'}
    c = DummyDeviceControl(result_show=result_show)
    ifname = 'eth0'
    assert c.show(ifname) == result_show
    assert c.show_args == [ifname]


def test_show_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.show('eth0')


def test_show_when_no_arguments_are_passed():
    c = DummyDeviceControl()
    with pytest.raises(ValueError):
        c.show('eth0')


def test_show_all():
    result_show_all = [{'key': 'value'}]
    c = DummyDeviceControl(result_show_all=result_show_all)
    assert c.show_all() == result_show_all


def test_show_all_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.show_all()


def test_connect():
    c = DummyDeviceControl()
    ifname = 'eth0'
    c.connect(ifname)
    assert c.connect_args == [ifname]


def test_connect_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.connect('eth0')


def test_disconnect():
    c = DummyDeviceControl()
    ifname = 'eth0'
    c.disconnect(ifname)
    assert c.disconnect_args == [ifname]


def test_disconnect_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.disconnect('eth0')


def test_reapply():
    c = DummyDeviceControl()
    ifname = 'eth0'
    c.reapply(ifname)
    assert c.reapply_args == [ifname]


def test_reapply_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.reapply('eth0')


def test_delete():
    c = DummyDeviceControl()
    ifname = 'eth0'
    c.delete(ifname)
    assert c.delete_args == [ifname]


def test_delete_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.delete('eth0')


def test_wifi():
    result_wifi = [DeviceWifi(False, 'ssid', '00:00:00:00:00:00', 'Infra', 1, 2400, 54, 78, 'WPA2')]
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


def test_wifi_hotspot():
    ifname = 'wlan0'
    con_name = 'MyHotspot'
    ssid = 'ssid'
    band = 'a'
    channel = 123
    password = 'passwd'
    r = Hotspot(ifname, con_name, ssid, password)
    c = DummyDeviceControl(result_wifi_hotspot=r)
    assert c.wifi_hotspot(ifname, con_name, ssid, band, channel, password) == r
    assert c.wifi_hotspot_args == [
        (ifname, con_name, ssid, band, channel, password)]


def test_wifi_hotspot_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.wifi_hotspot()


def test_wifi_hotspot_when_no_arguments_are_passed():
    c = DummyDeviceControl()
    with pytest.raises(ValueError):
        c.wifi_hotspot()


def test_wifi_rescan():
    c = DummyDeviceControl()
    ifname = 'wlan0'
    ssid = 'ssid'
    c.wifi_rescan(ifname, ssid)
    assert c.wifi_rescan_args == [(ifname, ssid)]


def test_wifi_rescan_when_raise_error():
    c = DummyDeviceControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.wifi_rescan()
