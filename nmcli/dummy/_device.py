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
    def wifi_connect_args(self):
        return self._wifi_connect_args

    def __init__(self,
                 result_call: List[Device] = None,
                 result_show: DeviceDetails = None,
                 result_show_all: List[DeviceDetails] = None,
                 result_wifi: List[DeviceWifi] = None,
                 raise_error: Exception = None):
        self._raise_error = raise_error
        self._result_call = result_call or []
        self._result_wifi = result_wifi or []
        self._result_show = result_show
        self._result_show_all = result_show_all or []
        self._show_args: List[str] = []
        self._connect_args: List[str] = []
        self._disconnect_args: List[str] = []
        self._reapply_args: List[str] = []
        self._delete_args: List[str] = []
        self._wifi_connect_args: List[Tuple] = []

    def __call__(self) -> List[Device]:
        self._raise_error_if_needed()
        return self._result_call

    def status(self) -> List[Device]:
        self._raise_error_if_needed()
        return self._result_call

    def show(self, ifname: str) -> DeviceDetails:
        self._raise_error_if_needed()
        self._show_args.append(ifname)
        if not self._result_show is None:
            return self._result_show
        raise ValueError("'result_show' is not properly initialized")

    def show_all(self) -> List[DeviceDetails]:
        self._raise_error_if_needed()
        return self._result_show_all

    def connect(self, ifname: str) -> None:
        self._raise_error_if_needed()
        self._connect_args.append(ifname)

    def disconnect(self, ifname: str) -> None:
        self._raise_error_if_needed()
        self._disconnect_args.append(ifname)

    def reapply(self, ifname: str) -> None:
        self._raise_error_if_needed()
        self._reapply_args.append(ifname)

    def delete(self, ifname: str) -> None:
        self._raise_error_if_needed()
        self._delete_args.append(ifname)

    def wifi(self) -> List[DeviceWifi]:
        self._raise_error_if_needed()
        return self._result_wifi

    def wifi_connect(self, ssid: str, password: str) -> None:
        self._raise_error_if_needed()
        self._wifi_connect_args.append((ssid, password))

    def wifi_hotspot(self,
                     ifname: str = None,
                     con_name: str = None,
                     ssid: str = None,
                     band: str = None,
                     channel: int = None,
                     password: str = None) -> Hotspot:
        raise NotImplementedError

    def _raise_error_if_needed(self):
        if not self._raise_error is None:
            raise self._raise_error
