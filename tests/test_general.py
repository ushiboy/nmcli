from nmcli._const import NetworkConnectivity
from nmcli._general import GeneralControl
from nmcli.data import General
from .helper import DummySystemCommand

def test_general():
    s = DummySystemCommand('''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
connected  full          enabled  enabled  enabled  enabled''')
    general = GeneralControl(s)
    r = general()
    assert r == General('connected', NetworkConnectivity.FULL, True, True, True, True)
    assert s.passed_parameters == ['general', 'status']

def test_general_status():
    s = DummySystemCommand('''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
connected  full          enabled  enabled  enabled  enabled''')
    general = GeneralControl(s)
    r = general.status()
    assert r == General('connected', NetworkConnectivity.FULL, True, True, True, True)
    assert s.passed_parameters == ['general', 'status']
