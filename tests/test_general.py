from nmcli._const import NetworkManagerState, NetworkConnectivity
from nmcli._general import GeneralControl
from nmcli.data import General
from .helper import DummySystemCommand

def test_general():
    s = DummySystemCommand('''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
connected  full          enabled  enabled  enabled  enabled''')
    general = GeneralControl(s)
    r = general()
    assert r == General(NetworkManagerState.CONNECTED_GLOBAL,
                        NetworkConnectivity.FULL, True, True, True, True)
    assert s.passed_parameters == ['general', 'status']

def test_status():
    s = DummySystemCommand('''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
connected  full          enabled  enabled  enabled  enabled''')
    general = GeneralControl(s)
    r = general.status()
    assert r == General(NetworkManagerState.CONNECTED_GLOBAL,
                        NetworkConnectivity.FULL, True, True, True, True)
    assert s.passed_parameters == ['general', 'status']

def test_get_hostname():
    s = DummySystemCommand('test\n')
    general = GeneralControl(s)
    assert general.get_hostname() == 'test'
    assert s.passed_parameters == ['general', 'hostname']

def test_set_hostname():
    s = DummySystemCommand()
    general = GeneralControl(s)
    general.set_hostname('test')
    assert s.passed_parameters == ['general', 'hostname', 'test']
