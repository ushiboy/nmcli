from nmcli._device import DeviceControl
from nmcli.data import Device, DeviceWifi
from .helper import DummySystemCommand

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
    assert s.passed_parameters == ['device', 'status']

def test_status():
    s = DummySystemCommand('''DEVICE  TYPE      STATE      CONNECTION
eth0    ethernet  connected  Default
wlan0   wifi      connected  MyWifi
lo      loopback  unmanaged  --''')
    device = DeviceControl(s)
    r = device.status()
    assert len(r) == 3
    assert r == [
        Device('eth0', 'ethernet', 'connected', 'Default'),
        Device('wlan0', 'wifi', 'connected', 'MyWifi'),
        Device('lo', 'loopback', 'unmanaged', None)
    ]
    assert s.passed_parameters == ['device', 'status']

def test_show():
    d = '''GENERAL.DEVICE:                         lo
GENERAL.TYPE:                           loopback
GENERAL.HWADDR:                         00:00:00:00:00:00
GENERAL.MTU:                            65536
GENERAL.STATE:                          10 (unmanaged)
GENERAL.CONNECTION:                     --
GENERAL.CON-PATH:                       --
IP4.ADDRESS[1]:                         127.0.0.1/8
IP4.GATEWAY:                            --
IP6.ADDRESS[1]:                         ::1/128
IP6.GATEWAY:                            --
IP6.ROUTE[1]:                           dst = ::1/128, nh = ::, mt = 256'''
    s = DummySystemCommand(d)
    device = DeviceControl(s)
    assert device.show('lo') == {
        'GENERAL.DEVICE': 'lo',
        'GENERAL.TYPE': 'loopback',
        'GENERAL.HWADDR': '00:00:00:00:00:00',
        'GENERAL.MTU': '65536',
        'GENERAL.STATE': '10 (unmanaged)',
        'GENERAL.CONNECTION': None,
        'GENERAL.CON-PATH': None,
        'IP4.ADDRESS[1]': '127.0.0.1/8',
        'IP4.GATEWAY': None,
        'IP6.ADDRESS[1]': '::1/128',
        'IP6.GATEWAY': None,
        'IP6.ROUTE[1]': 'dst = ::1/128, nh = ::, mt = 256'
        }
    assert s.passed_parameters == ['device', 'show', 'lo']

def test_show_all():
    d = '''GENERAL.DEVICE:                         wlan0
GENERAL.TYPE:                           wifi
GENERAL.HWADDR:                         46:7B:1F:32:36:E2
GENERAL.MTU:                            1500
GENERAL.STATE:                          30 (disconnected)
GENERAL.CONNECTION:                     --
GENERAL.CON-PATH:                       --

GENERAL.DEVICE:                         lo
GENERAL.TYPE:                           loopback
GENERAL.HWADDR:                         00:00:00:00:00:00
GENERAL.MTU:                            65536
GENERAL.STATE:                          10 (unmanaged)
GENERAL.CONNECTION:                     --
GENERAL.CON-PATH:                       --
IP4.ADDRESS[1]:                         127.0.0.1/8
IP4.GATEWAY:                            --
IP6.ADDRESS[1]:                         ::1/128
IP6.GATEWAY:                            --
IP6.ROUTE[1]:                           dst = ::1/128, nh = ::, mt = 256'''
    s = DummySystemCommand(d)
    device = DeviceControl(s)
    assert device.show_all() == [{
        'GENERAL.DEVICE': 'wlan0',
        'GENERAL.TYPE': 'wifi',
        'GENERAL.HWADDR': '46:7B:1F:32:36:E2',
        'GENERAL.MTU': '1500',
        'GENERAL.STATE': '30 (disconnected)',
        'GENERAL.CONNECTION': None,
        'GENERAL.CON-PATH': None
        }, {
        'GENERAL.DEVICE': 'lo',
        'GENERAL.TYPE': 'loopback',
        'GENERAL.HWADDR': '00:00:00:00:00:00',
        'GENERAL.MTU': '65536',
        'GENERAL.STATE': '10 (unmanaged)',
        'GENERAL.CONNECTION': None,
        'GENERAL.CON-PATH': None,
        'IP4.ADDRESS[1]': '127.0.0.1/8',
        'IP4.GATEWAY': None,
        'IP6.ADDRESS[1]': '::1/128',
        'IP6.GATEWAY': None,
        'IP6.ROUTE[1]': 'dst = ::1/128, nh = ::, mt = 256'
        }]
    assert s.passed_parameters == ['device', 'show']

def test_connect():
    s = DummySystemCommand()
    device = DeviceControl(s)
    ifname = 'eth0'
    device.connect(ifname)
    assert s.passed_parameters == ['device', 'connect', ifname]

def test_disconnect():
    s = DummySystemCommand()
    device = DeviceControl(s)
    ifname = 'eth0'
    device.disconnect(ifname)
    assert s.passed_parameters == ['device', 'disconnect', ifname]

def test_reapply():
    s = DummySystemCommand()
    device = DeviceControl(s)
    ifname = 'eth0'
    device.reapply(ifname)
    assert s.passed_parameters == ['device', 'reapply', ifname]

def test_delete():
    s = DummySystemCommand()
    device = DeviceControl(s)
    ifname = 'eth0'
    device.delete(ifname)
    assert s.passed_parameters == ['device', 'delete', ifname]

def test_device_wifi():
    d = '''IN-USE  SSID             MODE   CHAN  RATE        SIGNAL  BARS  SECURITY
*       AP1  Infra  1     130 Mbit/s  82      ______  WPA1 WPA2
        AP2  Infra  11    195 Mbit/s  74      ______  WPA2
        AP3  Infra  11    195 Mbit/s  72      ______  WPA1 WPA2'''
    s = DummySystemCommand(d)
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
