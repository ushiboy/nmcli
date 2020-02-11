from .helper import DummySystemCommand
from nmcli._connection import ConnectionControl
from nmcli.data import Connection
import pytest

def test_connection():
    s = DummySystemCommand('''NAME            UUID                                  TYPE      DEVICE
AP1  3eac760c-de77-4823-9ab8-773c276daca3  wifi      wlan0
Home            700f5b18-cbb3-4d38-9c61-e3bc3a3852b9  ethernet  eth0
''')
    connection = ConnectionControl(s)
    r = connection()

    assert r == [
        Connection('AP1', '3eac760c-de77-4823-9ab8-773c276daca3', 'wifi', 'wlan0'),
        Connection('Home', '700f5b18-cbb3-4d38-9c61-e3bc3a3852b9', 'ethernet', 'eth0')
    ]
    assert s.passed_parameters == 'connection'

def test_add():
    s = DummySystemCommand()
    connection = ConnectionControl(s)
    conn_type = 'ethernet'
    name = 'Con1'
    ifname = 'eth0'
    options = {
        'ipv4.addresses': '192.168.1.1/24',
        'ipv4.gateway': '192.168.1.255',
        'ipv4.method': 'manual'
    }
    connection.add(conn_type, ifname=ifname, name=name, options=options)
    assert s.passed_parameters == [
            'connection', 'add', 'type', conn_type, 'ifname', ifname,
            'con-name', name, 'ipv4.addresses', '192.168.1.1/24',
            'ipv4.gateway', '192.168.1.255', 'ipv4.method', 'manual']

    connection.add(conn_type)
    assert s.passed_parameters == [
            'connection', 'add', 'type', conn_type, 'ifname', '*']

def test_modify():
    s = DummySystemCommand()
    connection = ConnectionControl(s)
    name = 'Con1'
    options = {
        'ipv4.addresses': '192.168.1.1/24',
        'ipv4.gateway': '192.168.1.255',
        'ipv4.method': 'manual'
    }
    connection.modify(name, options)
    assert s.passed_parameters == [
            'connection', 'modify', name, 'ipv4.addresses', '192.168.1.1/24',
            'ipv4.gateway', '192.168.1.255', 'ipv4.method', 'manual']

def test_delete():
    s = DummySystemCommand()
    connection = ConnectionControl(s)
    name = 'Con1'
    connection.delete(name)
    assert s.passed_parameters == ['connection', 'delete', name]

def test_up():
    s = DummySystemCommand()
    connection = ConnectionControl(s)
    name = 'Con1'
    connection.up(name)
    assert s.passed_parameters == ['connection', 'up', name]

def test_down():
    s = DummySystemCommand()
    connection = ConnectionControl(s)
    name = 'Con1'
    connection.down(name)
    assert s.passed_parameters == ['connection', 'down', name]
