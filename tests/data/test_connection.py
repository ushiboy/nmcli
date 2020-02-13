from nmcli.data import Connection

def test_to_json():
    name = 'con'
    uuid = 'abcdef'
    conn_type = 'ethernet'
    device = 'eth0'
    c = Connection(name, uuid, conn_type, device)
    assert c.to_json() == {
        'name':name,
        'uuid':uuid,
        'conn_type':conn_type,
        'device':device
    }
