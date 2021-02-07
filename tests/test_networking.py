from nmcli._const import NetworkConnectivity
from nmcli._networking import NetworkingControl

from .helper import DummySystemCommand


def test_networking():
    s = DummySystemCommand('full\n')
    networking = NetworkingControl(s)
    r = networking()
    assert r == NetworkConnectivity.FULL
    assert s.passed_parameters == ['networking', 'connectivity']

def test_networking_connectivity():
    s = DummySystemCommand('full\n')
    networking = NetworkingControl(s)
    r = networking.connectivity()
    assert r == NetworkConnectivity.FULL
    assert s.passed_parameters == ['networking', 'connectivity']

    assert NetworkingControl(DummySystemCommand('unknown\n')).connectivity() \
            == NetworkConnectivity.UNKNOWN
    assert NetworkingControl(DummySystemCommand('none\n')).connectivity() \
            == NetworkConnectivity.NONE
    assert NetworkingControl(DummySystemCommand('portal\n')).connectivity() \
            == NetworkConnectivity.PORTAL
    assert NetworkingControl(DummySystemCommand('limited\n')).connectivity() \
            == NetworkConnectivity.LIMITED

def test_networking_connectivity_check():
    s = DummySystemCommand('full\n')
    networking = NetworkingControl(s)
    r = networking.connectivity(True)
    assert r == NetworkConnectivity.FULL
    assert s.passed_parameters == ['networking', 'connectivity', 'check']

def test_networking_on():
    s = DummySystemCommand()
    networking = NetworkingControl(s)
    networking.on()
    assert s.passed_parameters == ['networking', 'on']

def test_networking_off():
    s = DummySystemCommand()
    networking = NetworkingControl(s)
    networking.off()
    assert s.passed_parameters == ['networking', 'off']
