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
| general | status | supported |
| general | hostname | supported |
| general | permissions | not supported |
| general | logging | not supported |
| networking | | supported |
| networking | on | supported |
| networking | off | supported |
| networking | connectivity | supported |
| radio | | supported |
| radio | all | supported |
| radio | wifi | supported |
| radio | wwan | supported |
| connection | | supported |
| connection | show | supported |
| connection | up | supported |
| connection | down | supported |
| connection | add | supported |
| connection | modify | supported |
| connection | clone | not supported |
| connection | edit | not supported |
| connection | delete | supported |
| connection | reload | supported |
| connection | load | not supported |
| connection | import | not supported |
| connection | export | not supported |
| device | | supported |
| device | status | supported |
| device | show | supported |
| device | set | not supported |
| device | connect | supported |
| device | reapply | supported |
| device | modify | not supported |
| device | disconnect | supported |
| device | delete | supported |
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

#### nmcli.connection.reload

Reload all connection files from disk.

```
nmcli.connection.reload() -> None
```

### device

#### nmcli.device

Print status of devices.

```
nmcli.device() -> List[Device]
```

#### nmcli.device.status

Show status for all devices.

```
nmcli.device.status() -> List[Device]
```

#### nmcli.device.show

Show details of device.

```
nmcli.device.show(ifname: str) -> DeviceDetails
```

#### nmcli.device.show_all

Show details of devices.

```
nmcli.device.show_all() -> List[DeviceDetails]
```

#### nmcli.device.connect

Connect the device.

```
nmcli.device.connect(ifname: str) -> None
```

#### nmcli.device.disconnect

Disconnect devices.

```
nmcli.device.disconnect(ifname: str) -> None
```

#### nmcli.device.reapply

Attempts to update device with changes to the currently active connection made since it was last applied.

```
nmcli.device.reapply(ifname: str) -> None
```

#### nmcli.device.delete

Delete the software devices.

```
nmcli.device.delete(ifname: str) -> None
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

#### nmcli.general.status

Show overall status of NetworkManager.

```
nmcli.general.status() -> General
```

#### nmcli.general.get_hostname

Get persistent system hostname.

```
nmcli.general.get_hostname() -> str
```

#### nmcli.general.set_hostname

Change persistent system hostname.

```
nmcli.general.set_hostname(hostname: str) -> None
```

### networking

#### nmcli.networking

Get network connectivity state.

```
nmcli.networking() -> NetworkConnectivity
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
nmcli.networking.connectivity(check:bool = False) -> NetworkConnectivity
```

### radio

#### nmcli.radio

Get status of all radio switches.

```
nmcli.radio() -> Radio
```

#### nmcli.radio.all

Get status of all radio switches.

```
nmcli.radio.all() -> Radio
```

#### nmcli.radio.all_on

Turn on all radio switches.

```
nmcli.radio.all_on() -> None
```

#### nmcli.radio.all_off

Turn off all radio switches.

```
nmcli.radio.all_off() -> None
```

#### nmcli.radio.wifi

Get status of Wi-Fi radio switch.

```
nmcli.radio.wifi() -> bool
```

#### nmcli.radio.wifi_on

Turn on Wi-Fi radio switches.

```
nmcli.radio.wifi_on() -> None
```

#### nmcli.radio.wifi_off

Turn off Wi-Fi radio switches.

```
nmcli.radio.wifi_off() -> None
```

#### nmcli.radio.wwan

Get status of mobile broadband radio switch.

```
nmcli.radio.wwan() -> bool
```

#### nmcli.radio.wwan_on

Turn on mobile broadband radio switches.

```
nmcli.radio.wwan_on() -> None
```

#### nmcli.radio.wwan_off

Turn off mobile broadband radio switches.

```
nmcli.radio.wwan_off() -> None
```

## Change Log

### 0.3.1

Fixed device status and device wifi parsing bug.

### 0.3.0

Added networking and radio APIs.

Added more APIs for connection, device and general.

Changed the properties of the General data class.

Changed throw a ValueError exception if the regular expression pattern is not matched.

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
