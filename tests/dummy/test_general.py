import pytest

from nmcli._const import NetworkConnectivity, NetworkManagerState
from nmcli.data import General
from nmcli.dummy._general import DummyGeneralControl


def test_call():
    result_call = General(NetworkManagerState.CONNECTED_GLOBAL,
                          NetworkConnectivity.FULL,
                          True, True, True, True)
    c = DummyGeneralControl(result_call)
    assert c() == result_call

def test_call_when_raise_error():
    c = DummyGeneralControl(raise_error=Exception)
    with pytest.raises(Exception):
        c()

def test_call_when_no_arguments_are_passed():
    c = DummyGeneralControl()
    with pytest.raises(ValueError):
        c()

def test_status():
    result_status = General(NetworkManagerState.CONNECTED_GLOBAL,
                          NetworkConnectivity.FULL,
                          True, True, True, True)
    c = DummyGeneralControl(result_status=result_status)
    assert c.status() == result_status

def test_status_when_raise_error():
    c = DummyGeneralControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.status()

def test_status_when_no_arguments_are_passed():
    c = DummyGeneralControl()
    with pytest.raises(ValueError):
        c.status()

def test_get_hostname():
    result_hostname = 'test'
    c = DummyGeneralControl(result_hostname=result_hostname)
    assert c.get_hostname() == result_hostname

def test_get_hostname_when_raise_error():
    c = DummyGeneralControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.get_hostname()

def test_set_hostname():
    hostname = 'test'
    c = DummyGeneralControl()
    c.set_hostname(hostname)
    assert c.set_hostname_args == [hostname]

def test_set_hostname_when_raise_error():
    c = DummyGeneralControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.set_hostname('')
