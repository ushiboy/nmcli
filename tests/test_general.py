from nmcli._const import NetworkManagerState, NetworkConnectivity
from nmcli._general import GeneralControl
from nmcli.data import General
from .helper import DummySystemCommand

def st(data):
    return GeneralControl(DummySystemCommand(data)).status()

def test_general():
    s = DummySystemCommand('''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
connected  full          enabled  enabled  enabled  enabled''')
    general = GeneralControl(s)
    r = general()
    assert r == General(NetworkManagerState.CONNECTED_GLOBAL,
                        NetworkConnectivity.FULL, True, True, True, True)
    assert s.passed_parameters == ['general', 'status']

def test_general_status():
    s = DummySystemCommand('''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
connected  full          enabled  enabled  enabled  enabled''')
    general = GeneralControl(s)
    r = general.status()
    assert r == General(NetworkManagerState.CONNECTED_GLOBAL,
                        NetworkConnectivity.FULL, True, True, True, True)
    assert s.passed_parameters == ['general', 'status']

    d1 = '''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
unknown  none          enabled  enabled  enabled  disabled'''
    assert st(d1) == General(NetworkManagerState.UNKNOWN, NetworkConnectivity.NONE,
                             True, True, True, False)

    d2 = '''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
asleep  portal          enabled  enabled  disabled  enabled'''
    assert st(d2) == General(NetworkManagerState.ASLEEP, NetworkConnectivity.PORTAL,
                             True, True, False, True)

    d3 = '''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
connecting  limited          enabled  disabled  enabled  enabled'''
    assert st(d3) == General(NetworkManagerState.CONNECTING, NetworkConnectivity.LIMITED,
                             True, False, True, True)

    d4 = '''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
connected (local only)  full          disabled  enabled  enabled  enabled'''
    assert st(d4) == General(NetworkManagerState.CONNECTED_LOCAL, NetworkConnectivity.FULL,
                             False, True, True, True)

    d5 = '''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
connected (site only)  full          enabled  enabled  enabled  enabled'''
    assert st(d5) == General(NetworkManagerState.CONNECTED_SITE, NetworkConnectivity.FULL,
                             True, True, True, True)

    d6 = '''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
disconnecting  full          enabled  enabled  enabled  enabled'''
    assert st(d6) == General(NetworkManagerState.DISCONNECTING, NetworkConnectivity.FULL,
                             True, True, True, True)

    d7 = '''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
disconnected  full          enabled  enabled  enabled  enabled'''
    assert st(d7) == General(NetworkManagerState.DISCONNECTED, NetworkConnectivity.FULL,
                             True, True, True, True)
