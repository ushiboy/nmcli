from nmcli._radio import RadioControl
from nmcli.data import Radio
from .helper import DummySystemCommand

def test_radio():
    s = DummySystemCommand('''WIFI-HW  WIFI     WWAN-HW  WWAN
enabled  enabled  enabled  enabled''')
    radio = RadioControl(s)
    r = radio()
    assert r == Radio(True, True, True, True)
    assert s.passed_parameters == ['radio', 'all']

def test_radio_all():
    s = DummySystemCommand('''WIFI-HW  WIFI     WWAN-HW  WWAN
enabled  disabled  enabled  disabled''')
    radio = RadioControl(s)
    r = radio.all()
    assert r == Radio(True, False, True, False)
    assert s.passed_parameters == ['radio', 'all']

def test_radio_all_on():
    s = DummySystemCommand()
    radio = RadioControl(s)
    radio.all_on()
    assert s.passed_parameters == ['radio', 'all', 'on']

def test_radio_all_off():
    s = DummySystemCommand()
    radio = RadioControl(s)
    radio.all_off()
    assert s.passed_parameters == ['radio', 'all', 'off']

def test_radio_wifi():
    s = DummySystemCommand('enabled\n')
    radio = RadioControl(s)
    assert radio.wifi()
    assert s.passed_parameters == ['radio', 'wifi']
    assert not RadioControl(DummySystemCommand('disabled\n')).wifi()

def test_radio_wifi_on():
    s = DummySystemCommand()
    radio = RadioControl(s)
    radio.wifi_on()
    assert s.passed_parameters == ['radio', 'wifi', 'on']

def test_radio_wifi_off():
    s = DummySystemCommand()
    radio = RadioControl(s)
    radio.wifi_off()
    assert s.passed_parameters == ['radio', 'wifi', 'off']

def test_radio_wwan():
    s = DummySystemCommand('enabled\n')
    radio = RadioControl(s)
    assert radio.wwan()
    assert s.passed_parameters == ['radio', 'wwan']
    assert not RadioControl(DummySystemCommand('disabled\n')).wwan()

def test_radio_wwan_on():
    s = DummySystemCommand()
    radio = RadioControl(s)
    radio.wwan_on()
    assert s.passed_parameters == ['radio', 'wwan', 'on']

def test_radio_wwan_off():
    s = DummySystemCommand()
    radio = RadioControl(s)
    radio.wwan_off()
    assert s.passed_parameters == ['radio', 'wwan', 'off']
