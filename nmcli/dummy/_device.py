from typing import List, Tuple

from .._device import DeviceControlInterface, DeviceDetails
from ..data.device import Device, DeviceWifi
from ..data.hotspot import Hotspot


class DummyDeviceControl(DeviceControlInterface):

    @property
    def show_args(self):
        return self._show_args

    @property
    def connect_args(self):
        return self._connect_args

    @property
    def disconnect_args(self):
        return self._disconnect_args

    @property
    def reapply_args(self):
        return self._reapply_args

    @property
    def delete_args(self):
        return self._delete_args

    @property
    def wifi_args(self):
        return self._wifi_args

    @property
    def wifi_connect_args(self):
        return self._wifi_connect_args

    @property
    def wifi_hotspot_args(self):
        return self._wifi_hotspot_args

    @property
    def wifi_rescan_args(self):
        return self._wifi_rescan_args

    def __init__(self,
                 result_call: List[Device] = None,
                 result_show: DeviceDetails = None,
                 result_show_all: List[DeviceDetails] = None,
                 result_wifi: List[DeviceWifi] = None,
                 result_wifi_hotspot: Hotspot = None,
                 raise_error: Exception = None):
        self._raise_error = raise_error
        self._result_call = result_call or []
        self._result_wifi = result_wifi or []
        self._result_show = result_show
        self._result_show_all = result_show_all or []
        self._result_wifi_hotspot = result_wifi_hotspot
        self._show_args: List[Tuple] = []
        self._connect_args: List[Tuple] = []
        self._disconnect_args: List[Tuple] = []
        self._reapply_args: List[str] = []
        self._delete_args: List[Tuple] = []
        self._wifi_args: List[Tuple] = []
        self._wifi_connect_args: List[Tuple] = []
        self._wifi_hotspot_args: List[Tuple] = []
        self._wifi_rescan_args: List[Tuple] = []

    def __call__(self) -> List[Device]:
        self._raise_error_if_needed()
        return self._result_call

    def status(self) -> List[Device]:
        self._raise_error_if_needed()
        return self._result_call

    def show(self, ifname: str, fields: str = None) -> DeviceDetails:
        self._raise_error_if_needed()
        self._show_args.append((ifname, fields))
        if not self._result_show is None:
            return self._result_show
        raise ValueError("'result_show' is not properly initialized")

    def show_all(self, fields: str = None) -> List[DeviceDetails]:
        self._raise_error_if_needed()
        return self._result_show_all

    def connect(self, ifname: str, wait: int = None) -> None:
        self._raise_error_if_needed()
        self._connect_args.append((ifname, wait))

    def disconnect(self, ifname: str, wait: int = None) -> None:
        self._raise_error_if_needed()
        self._disconnect_args.append((ifname, wait))

    def reapply(self, ifname: str) -> None:
        self._raise_error_if_needed()
        self._reapply_args.append(ifname)

    def delete(self, ifname: str, wait: int = None) -> None:
        self._raise_error_if_needed()
        self._delete_args.append((ifname, wait))

    def wifi(self, ifname: str = None, rescan: bool = None) -> List[DeviceWifi]:
        self._raise_error_if_needed()
        self._wifi_args.append((ifname, rescan))
        return self._result_wifi

    def wifi_connect(self,
                     ssid: str,
                     password: str,
                     ifname: str = None,
                     wait: int = None) -> None:
        self._raise_error_if_needed()
        self._wifi_connect_args.append((ssid, password, ifname, wait))

    def wifi_hotspot(self,
                     ifname: str = None,
                     con_name: str = None,
                     ssid: str = None,
                     band: str = None,
                     channel: int = None,
                     password: str = None) -> Hotspot:
        self._raise_error_if_needed()
        self._wifi_hotspot_args.append(
            (ifname, con_name, ssid, band, channel, password))
        if not self._result_wifi_hotspot is None:
            return self._result_wifi_hotspot
        raise ValueError("'result_wifi_hotspot' is not properly initialized")

    def wifi_rescan(self,
                    ifname: str = None,
                    ssid: str = None) -> None:
        self._raise_error_if_needed()
        self._wifi_rescan_args.append((ifname, ssid))

    def _raise_error_if_needed(self):
        if not self._raise_error is None:
            raise self._raise_error
