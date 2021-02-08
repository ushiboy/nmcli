from nmcli.data import Connection


def test_to_json():
    name = 'con'
    uuid = 'abcdef'
    conn_type = 'ethernet'
    device = 'eth0'
    c = Connection(name, uuid, conn_type, device)
    assert c.to_json() == {
        'name': name,
        'uuid': uuid,
        'conn_type': conn_type,
        'device': device
    }


def test_parse():
    d1 = 'AP1  3eac760c-de77-4823-9ab8-773c276daca3  wifi      wlan0'
    assert Connection.parse(d1) == \
        Connection('AP1', '3eac760c-de77-4823-9ab8-773c276daca3',
                   'wifi', 'wlan0')
    d2 = 'Home            700f5b18-cbb3-4d38-9c61-e3bc3a3852b9  ethernet  eth0'
    assert Connection.parse(d2) == \
        Connection('Home', '700f5b18-cbb3-4d38-9c61-e3bc3a3852b9',
                   'ethernet', 'eth0')
    d3 = 'Wired connection 1  700f5b18-cbb3-4d38-9c61-999999999999  ethernet  eth1'
    assert Connection.parse(d3) == \
        Connection('Wired connection 1',
                   '700f5b18-cbb3-4d38-9c61-999999999999', 'ethernet', 'eth1')
