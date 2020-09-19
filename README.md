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

## Compatibility table

| Object | Command | Status |
|--------|---------|--------|
| general | | supported |
| general | status | not supported |
| general | hostname | not supported |
| general | permissions | not supported |
| general | logging | not supported |
| networking | | supported |
| networking | on | supported |
| networking | off | supported |
| networking | connectivity | supported |
| radio | | not supported |
| radio | all | not supported |
| radio | wifi | not supported |
| radio | wwan | not supported |
| connection | | supported |
| connection | show | supported |
| connection | up | supported |
| connection | down | supported |
| connection | add | supported |
| connection | modify | supported |
| connection | clone | not supported |
| connection | edit | not supported |
| connection | delete | supported |
| connection | reload | not supported |
| connection | load | not supported |
| connection | import | not supported |
| connection | export | not supported |
| device | | supported |
| device | status | not supported |
| device | show | not supported |
| device | set | not supported |
| device | connect | not supported |
| device | reapply | not supported |
| device | modify | not supported |
| device | disconnect | not supported |
| device | delete | not supported |
| device | monitor | not supported |
| device | wifi | supported |
| device | wifi connect | supported |
| device | wifi rescan | not supported |
| device | lldp hotspot | not supported |
| agent | | not supported |
| agent | secret | not supported |
| agent | polkit | not supported |
| agent | all | not supported |
| monitor | | not supported |


## API

### connection

#### nmcli.connection

Get a list of connections.

```
nmcli.connection() -> List[Connection]
```

#### nmcli.connection.add

Create a new connection using specified properties.

```
nmcli.connection.add(
    conn_type: str,
    options: Optional[ConnectionOptions] = None,
    ifname: str = "*",
    name: str = None,
    autoconnect: bool = False) -> None
```

#### nmcli.connection.modify

Add, modify or remove properties in the connection profile.

```
nmcli.connection.modify(name: str, options: ConnectionOptions) -> None
```

#### nmcli.connection.delete

Delete a configured connection.

```
nmcli.connection.delete(name: str) -> None
```

#### nmcli.connection.up

Activate a connection.

```
nmcli.connection.up(name: str) -> None
```

#### nmcli.connection.down

Deactivate a connection from a device without preventing the device from further auto-activation.

```
nmcli.connection.down(name: str) -> None
```

#### nmcli.connection.show

Show details for specified connections.

```
nmcli.connection.show(name: str) -> ConnectionDetails
```

### device

#### nmcli.device

Print status of devices.

```
nmcli.device() -> List[Device]
```

#### nmcli.device.wifi

List available Wi-Fi access points.

```
nmcli.device.wifi() -> List[DeviceWifi]
```

#### nmcli.device.wifi_connect

Connect to a Wi-Fi network specified by SSID or BSSID.

```
nmcli.device.wifi_connect(ssid: str, password: str) -> None
```

### general

#### nmcli.general

Show overall status of NetworkManager.

```
nmcli.general() -> General
```

### networking

#### nmcli.networking

Get network connectivity state.

```
nmcli.networking() -> str
```

#### nmcli.networking.on

Switch networking on.

```
nmcli.networking.on() -> None
```

#### nmcli.networking.off

Switch networking off.

```
nmcli.networking.off() -> None
```

#### nmcli.networking.connectivity

Get network connectivity state.

The optional 'check' argument makes NetworkManager re-check the connectivity.

```
nmcli.networking.connectivity(check:bool = False) -> str
```


## Change Log

### 0.2.2

Fix the parsing bug of connection names that contain spaces (connection.show).

Added getting items that begin with a capital letter.

### 0.2.1

Fix the parsing bug of connection names that contain spaces.

### 0.2.0

Added dummy classes.

### 0.1.0

Initial release.

## License

MIT
