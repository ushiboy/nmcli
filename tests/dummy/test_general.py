import pytest
from nmcli.dummy._general import DummyGeneralControl
from nmcli.data import General

def test_call():
    result_call = General('connected', 'full', 'enabled', 'enabled', 'enabled', 'enabled')
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
