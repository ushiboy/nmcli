import os

from nmcli._connection import ConnectionControl
from nmcli.data import Connection

from .helper import DummySystemCommand

connection_data_file = os.path.join(
    os.path.dirname(__file__), 'connection_data.txt')


def test_connection():
    s = DummySystemCommand('''NAME            UUID                                  TYPE      DEVICE
AP1  3eac760c-de77-4823-9ab8-773c276daca3  wifi      wlan0
Home            700f5b18-cbb3-4d38-9c61-e3bc3a3852b9  ethernet  eth0
Wired connection 1  700f5b18-cbb3-4d38-9c61-999999999999  ethernet  eth1''')
    connection = ConnectionControl(s)
    r = connection()

    assert r == [
        Connection('AP1', '3eac760c-de77-4823-9ab8-773c276daca3',
                   'wifi', 'wlan0'),
        Connection('Home', '700f5b18-cbb3-4d38-9c61-e3bc3a3852b9',
                   'ethernet', 'eth0'),
        Connection('Wired connection 1',
                   '700f5b18-cbb3-4d38-9c61-999999999999', 'ethernet', 'eth1')
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

    connection.add(conn_type, autoconnect=True)
    assert s.passed_parameters == [
        'connection', 'add', 'type', conn_type, 'ifname', '*', 'autoconnect', 'yes']

    connection.add(conn_type, autoconnect=False)
    assert s.passed_parameters == [
        'connection', 'add', 'type', conn_type, 'ifname', '*', 'autoconnect', 'no']


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

    connection.delete(name, wait=10)
    assert s.passed_parameters == [
        '--wait', '10', 'connection', 'delete', name]


def test_up():
    s = DummySystemCommand()
    connection = ConnectionControl(s)
    name = 'Con1'
    connection.up(name)
    assert s.passed_parameters == ['connection', 'up', name]

    connection.up(name, wait=10)
    assert s.passed_parameters == ['--wait', '10', 'connection', 'up', name]


def test_down():
    s = DummySystemCommand()
    connection = ConnectionControl(s)
    name = 'Con1'
    connection.down(name)
    assert s.passed_parameters == ['connection', 'down', name]

    connection.down(name, wait=10)
    assert s.passed_parameters == ['--wait', '10', 'connection', 'down', name]


def test_show():
    with open(connection_data_file, encoding='utf-8') as f:
        buf = f.read()
    s = DummySystemCommand(buf)
    connection = ConnectionControl(s)
    name = 'Wired connection 1'

    r = connection.show(name)
    assert s.passed_parameters == ['connection', 'show', name]
    assert len(r.keys()) == 114
    assert r['connection.id'] == 'Wired connection 1'
    assert r['connection.stable-id'] is None
    assert r['ipv4.dns-options'] is None
    assert r['IP4.ADDRESS[1]'] == '192.168.1.10/24'
    assert r['DHCP6.OPTION[8]'] == 'requested_dhcp6_name_servers = 1'

    connection.show(name, show_secrets=True)
    assert s.passed_parameters == [
        'connection', 'show', name, "--show-secrets"]


def test_reload():
    s = DummySystemCommand()
    connection = ConnectionControl(s)
    connection.reload()
    assert s.passed_parameters == ['connection', 'reload']
