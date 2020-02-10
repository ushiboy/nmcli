from .helper import DummySystemCommand
from nmcli._general import GeneralControl
from nmcli.data import General
import pytest

def test_general():
    s = DummySystemCommand('''STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
connected  full          enabled  enabled  enabled  enabled''')
    general = GeneralControl(s)
    r = general()
    assert r == General('connected', 'full', 'enabled', 'enabled', 'enabled', 'enabled')
    assert s.passed_parameters == 'general'
