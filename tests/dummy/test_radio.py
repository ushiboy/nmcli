import pytest

from nmcli.data import Radio
from nmcli.dummy._radio import DummyRadioControl


def test_call():
    result_call = Radio(True, True, True, True)
    c = DummyRadioControl(result_call)
    assert c() == result_call

def test_call_when_raise_error():
    c = DummyRadioControl(raise_error=Exception)
    with pytest.raises(Exception):
        c()

def test_call_when_no_arguments_are_passed():
    c = DummyRadioControl()
    with pytest.raises(ValueError):
        c()

def test_all():
    result_all = Radio(True, True, True, True)
    c = DummyRadioControl(result_all=result_all)
    assert c.all() == result_all

def test_all_when_raise_error():
    c = DummyRadioControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.all()

def test_all_when_no_arguments_are_passed():
    c = DummyRadioControl()
    with pytest.raises(ValueError):
        c.all()

def test_all_on():
    c = DummyRadioControl()
    c.all_on()
    assert c.called_all_on == 1

def test_all_on_when_raise_error():
    c = DummyRadioControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.all_on()

def test_all_off():
    c = DummyRadioControl()
    c.all_off()
    assert c.called_all_off == 1

def test_all_off_when_raise_error():
    c = DummyRadioControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.all_off()

def test_wifi():
    result_wifi = True
    c = DummyRadioControl(result_wifi=result_wifi)
    assert c.wifi() == result_wifi

def test_wifi_when_raise_error():
    c = DummyRadioControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.wifi()

def test_wifi_when_no_arguments_are_passed():
    c = DummyRadioControl()
    with pytest.raises(ValueError):
        c.wifi()

def test_wifi_on():
    c = DummyRadioControl()
    c.wifi_on()
    assert c.called_wifi_on == 1

def test_wifi_on_when_raise_error():
    c = DummyRadioControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.wifi_on()

def test_wifi_off():
    c = DummyRadioControl()
    c.wifi_off()
    assert c.called_wifi_off == 1

def test_wifi_off_when_raise_error():
    c = DummyRadioControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.wifi_off()

def test_wwan():
    result_wwan = True
    c = DummyRadioControl(result_wwan=result_wwan)
    assert c.wwan() == result_wwan

def test_wwan_when_raise_error():
    c = DummyRadioControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.wwan()

def test_wwan_when_no_arguments_are_passed():
    c = DummyRadioControl()
    with pytest.raises(ValueError):
        c.wwan()

def test_wwan_on():
    c = DummyRadioControl()
    c.wwan_on()
    assert c.called_wwan_on == 1

def test_wwan_on_when_raise_error():
    c = DummyRadioControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.wwan_on()

def test_wwan_off():
    c = DummyRadioControl()
    c.wwan_off()
    assert c.called_wwan_off == 1

def test_wwan_off_when_raise_error():
    c = DummyRadioControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.wwan_off()
