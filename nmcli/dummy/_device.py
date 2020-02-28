from typing import List, Tuple
from .._device import DeviceControlInterface
from ..data.device import Device, DeviceWifi

class DummyDeviceControl(DeviceControlInterface):

    @property
    def wifi_connect_args(self):
        return self._wifi_connect_args

    def __init__(self, result_call: List[Device] = None,
                 result_wifi: List[DeviceWifi] = None, raise_error: Exception = None):
        self._raise_error = raise_error
        self._result_call = [] if result_call is None else result_call
        self._result_wifi = [] if result_wifi is None else result_wifi
        self._wifi_connect_args: List[Tuple] = []

    def __call__(self) -> List[Device]:
        if not self._raise_error is None:
            raise self._raise_error
        return self._result_call

    def wifi(self) -> List[DeviceWifi]:
        if not self._raise_error is None:
            raise self._raise_error
        return self._result_wifi

    def wifi_connect(self, ssid: str, password: str) -> None:
        if not self._raise_error is None:
            raise self._raise_error
        self._wifi_connect_args.append((ssid, password))
