import pytest

from nmcli._const import NetworkConnectivity, NetworkManagerState
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


def test_reload_without_flags():
    s = DummySystemCommand()
    general = GeneralControl(s)
    general.reload()
    assert s.passed_parameters == ['general', 'reload']


def test_reload_with_single_flag():
    s = DummySystemCommand()
    general = GeneralControl(s)
    general.reload(['conf'])
    assert s.passed_parameters == ['general', 'reload', 'conf']


def test_reload_with_all_valid_flags():
    s = DummySystemCommand()
    general = GeneralControl(s)
    general.reload(['conf', 'dns-rc', 'dns-full'])
    assert s.passed_parameters == ['general', 'reload', 'conf', 'dns-rc', 'dns-full']


def test_reload_with_invalid_flag():
    s = DummySystemCommand()
    general = GeneralControl(s)
    with pytest.raises(ValueError) as exc_info:
        general.reload(['invalid-flag'])
    assert "Invalid reload flag 'invalid-flag'" in str(exc_info.value)
    assert "Valid flags are: conf, dns-rc, dns-full" in str(exc_info.value)


def test_reload_with_mixed_valid_and_invalid_flags():
    s = DummySystemCommand()
    general = GeneralControl(s)
    with pytest.raises(ValueError) as exc_info:
        general.reload(['conf', 'invalid'])
    assert "Invalid reload flag 'invalid'" in str(exc_info.value)
