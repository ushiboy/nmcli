from nmcli._networking import NetworkingControl
from .helper import DummySystemCommand

def test_networking():
    s = DummySystemCommand('full\n')
    networking = NetworkingControl(s)
    r = networking()
    assert r == 'full'
    assert s.passed_parameters == ['networking', 'connectivity']

def test_networking_connectivity():
    s = DummySystemCommand('full\n')
    networking = NetworkingControl(s)
    r = networking.connectivity()
    assert r == 'full'
    assert s.passed_parameters == ['networking', 'connectivity']

def test_networking_connectivity_check():
    s = DummySystemCommand('full\n')
    networking = NetworkingControl(s)
    r = networking.connectivity(True)
    assert r == 'full'
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
