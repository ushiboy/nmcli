import os

from nmcli._device import DeviceControl
from nmcli.data import Device, DeviceWifi, Hotspot

from .helper import DummySystemCommand

device_data_file = os.path.join(os.path.dirname(__file__), 'device_data.txt')
device_wifi_data_file = os.path.join(os.path.dirname(__file__), 'device_wifi_data.txt')
device_wifi_data_include_bssid_file = os.path.join(os.path.dirname(__file__),
        'device_wifi_data_include_bssid.txt')

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
    with open(device_data_file) as f:
        buf = f.read()
    s = DummySystemCommand(buf)
    device = DeviceControl(s)
    r = device.status()
    assert len(r) == 4
    assert r == [
        Device('eth0', 'ethernet', 'connected', 'Wired connection 1'),
        Device('wlan0', 'wifi', 'disconnected', None),
        Device('p2p-dev-wlan0', 'wifi-p2p', 'disconnected', None),
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
    d = '''*:AP1:Infra:1:130 Mbit/s:82:WPA1 WPA2
 :AP2:Infra:11:195 Mbit/s:74:WPA2
 :AP3:Infra:11:195 Mbit/s:72:WPA1 WPA2'''
    s = DummySystemCommand(d)
    device = DeviceControl(s)
    r = device.wifi()
    assert len(r) == 3
    assert r == [
        DeviceWifi(True, 'AP1', 'Infra', 1, 130, 82, 'WPA1 WPA2'),
        DeviceWifi(False, 'AP2', 'Infra', 11, 195, 74, 'WPA2'),
        DeviceWifi(False, 'AP3', 'Infra', 11, 195, 72, 'WPA1 WPA2'),
    ]
    assert s.passed_parameters == ['-t', '-f', 'IN-USE,SSID,MODE,CHAN,RATE,SIGNAL,SECURITY',
            'device', 'wifi']

    with open(device_wifi_data_file) as f:
        buf = f.read()
    device = DeviceControl(DummySystemCommand(buf))
    r = device.wifi()
    assert len(r) == 3
    assert r == [
        DeviceWifi(False, 'AP1', 'Infra', 11, 195, 72, 'WPA1 WPA2'),
        DeviceWifi(False, 'AP2', 'Infra', 4, 130, 40, 'WPA1 WPA2'),
        DeviceWifi(False, 'AP3', 'Infra', 6, 65, 24, 'WPA2'),
    ]

def test_wifi_connect():
    s = DummySystemCommand()
    device = DeviceControl(s)
    ssid = 'AP1'
    password = 'abc'
    device.wifi_connect(ssid, password)
    assert s.passed_parameters == ['device', 'wifi', 'connect', ssid, 'password', password]

def test_wifi_hotspot():
    d1 = '''Hotspot password: abcdefgh
Device 'wlan0' successfully activated with '00000000-0000-0000-0000-000000000000'.
'''
    d2 = '''connection.id:Hotspot
802-11-wireless.ssid:AP1
'''
    s = DummySystemCommand([d1, d2])
    device = DeviceControl(s)
    r = device.wifi_hotspot()
    assert r == Hotspot('wlan0', 'Hotspot', 'AP1', 'abcdefgh')
    assert s.parameters_history == [
            ['device', 'wifi', 'hotspot', '--show-secrets'],
            ['-t', '-f', 'connection.id,802-11-wireless.ssid',
                'connection', 'show', 'uuid', '00000000-0000-0000-0000-000000000000']
            ]

    s2 = DummySystemCommand([d1, d2])
    ifname = 'wlan0'
    con_name = 'MyHotspot'
    ssid  ='Hot Spot'
    band = 'a'
    channel = 123
    password = 'pass'
    DeviceControl(s2).wifi_hotspot(ifname, con_name, ssid, band, channel, password)
    assert s2.parameters_history == [
            ['device', 'wifi', 'hotspot', '--show-secrets', 'ifname', ifname,
                'con-name', con_name, 'ssid', ssid, 'band', band,
                'channel', str(channel), 'password', password],
            ['-t', '-f', 'connection.id,802-11-wireless.ssid',
                'connection', 'show', 'uuid', '00000000-0000-0000-0000-000000000000']
            ]
