import pytest

from nmcli.data import Connection
from nmcli.dummy._connection import DummyConnectionControl


def test_call():
    result_call = [Connection('a', 'b', 'ethernet', 'eth0')]
    c = DummyConnectionControl(result_call)
    assert c() == result_call


def test_call_when_raise_error():
    c = DummyConnectionControl(raise_error=Exception)
    with pytest.raises(Exception):
        c()


def test_add():
    c = DummyConnectionControl()
    conn_type = 'ethernet'
    options = {
        'key': 'value'
    }
    ifname = 'eth0'
    name = 'MyHome'
    autoconnect = True
    c.add(conn_type, options, ifname, name, autoconnect)
    assert c.add_args[0] == (conn_type, options, ifname, name, autoconnect)

    c.add(conn_type, options, ifname, name, False)
    assert c.add_args[1] == (conn_type, options, ifname, name, False)

    c.add(conn_type, options, ifname, name)
    assert c.add_args[2] == (conn_type, options, ifname, name, None)


def test_add_when_raise_error():
    c = DummyConnectionControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.add('ethernet')


def test_modify():
    c = DummyConnectionControl()
    options = {
        'key': 'value'
    }
    name = 'MyHome'
    c.modify(name, options)
    assert c.modify_args[0] == (name, options)


def test_modify_when_raise_error():
    c = DummyConnectionControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.modify('ethernet', {'key': 'value'})


def test_delete():
    c = DummyConnectionControl()
    name = 'MyHome'
    c.delete(name)
    assert c.delete_args[0] == (name, None)

    c.delete(name, wait=10)
    assert c.delete_args[1] == (name, 10)


def test_delete_when_raise_error():
    c = DummyConnectionControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.delete('ethernet')


def test_up():
    c = DummyConnectionControl()
    name = 'MyHome'
    c.up(name)
    assert c.up_args[0] == (name, None)

    c.up(name, wait=10)
    assert c.up_args[1] == (name, 10)


def test_up_when_raise_error():
    c = DummyConnectionControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.up('ethernet')


def test_down():
    c = DummyConnectionControl()
    name = 'MyHome'
    c.down(name)
    assert c.down_args[0] == (name, None)

    c.down(name, wait=10)
    assert c.down_args[1] == (name, 10)


def test_down_when_raise_error():
    c = DummyConnectionControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.down('ethernet')


def test_show():
    result_show = {
        'key': 'value'
    }
    c = DummyConnectionControl(result_show=result_show)

    name = 'MyHome'
    assert c.show(name) == result_show
    assert c.show_args[0] == (name, False)

    c.show(name, show_secrets=True)
    assert c.show_args[1] == (name, True)


def test_show_when_raise_error():
    c = DummyConnectionControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.show('MyHome')


def test_show_when_no_arguments_are_passed():
    c = DummyConnectionControl()
    with pytest.raises(ValueError):
        c.show('MyHome')


def test_reload():
    c = DummyConnectionControl()
    c.reload()
    assert c.called_reload == 1


def test_reload_when_raise_error():
    c = DummyConnectionControl(raise_error=Exception)
    with pytest.raises(Exception):
        c.reload()
