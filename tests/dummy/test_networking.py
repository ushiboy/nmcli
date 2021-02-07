import pytest

from nmcli._const import NetworkConnectivity
from nmcli.dummy._networking import DummyNetworkingControl


def test_call():
    result_call = NetworkConnectivity.FULL
    c = DummyNetworkingControl(result_call)
    assert c() == result_call

def test_call_when_raise_error():
    c = DummyNetworkingControl(raise_error=Exception)
    with pytest.raises(Exception):
        c()

def test_call_when_no_arguments_are_passed():
    c = DummyNetworkingControl()
    with pytest.raises(ValueError):
        c()

def test_on():
    c = DummyNetworkingControl()
    c.on()
    assert c.called_on == 1

def test_on_when_raise_error():
    c = DummyNetworkingControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.on()

def test_off():
    c = DummyNetworkingControl()
    c.off()
    assert c.called_off == 1

def test_off_when_raise_error():
    c = DummyNetworkingControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.off()

def test_connectivity():
    result_connectivity = NetworkConnectivity.FULL
    c = DummyNetworkingControl(result_connectivity=result_connectivity)
    assert c.connectivity(True) == result_connectivity
    assert c.connectivity_args == [True]

def test_connectivity_when_raise_error():
    c = DummyNetworkingControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.connectivity()

def test_connectivity_when_no_arguments_are_passed():
    c = DummyNetworkingControl()
    with pytest.raises(ValueError):
        c.connectivity()
