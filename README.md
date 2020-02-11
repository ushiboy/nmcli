nmcli
=====

nmcli is a python wrapper library for the network-manager cli client.

## Quick Sample

Here is a simple usecase.

```python
import nmcli

try:
    print(nmcli.connection())
    print(nmcli.device())
    print(nmcli.device.wifi())
    print(nmcli.general())

    nmcli.device.wifi_connect('AP1', 'passphrase')
    nmcli.connection.modify('AP1', {
            'ipv4.addresses': '192.168.1.1/24',
            'ipv4.gateway': '192.168.1.255',
            'ipv4.method': 'manual'
        })
    nmcli.connection.down('AP1')
    nmcli.connection.up('AP1')
    nmcli.connection.delete('AP1')
except Exception as e:
    print(e)
```

## Dependency

* NetworkManager
  * `sudo apt install network-manager` (Debian)
* User who can execute nmcli with sudo with NOPASSWD

## API

wip

## Change Log

wip

## License

MIT
