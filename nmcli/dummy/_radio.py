from .._radio import RadioControlInterface
from ..data.radio import Radio

class DummyRadioControl(RadioControlInterface):

    @property
    def called_all_on(self) -> int:
        return self._called_all_on

    @property
    def called_all_off(self) -> int:
        return self._called_all_off

    @property
    def called_wifi_on(self) -> int:
        return self._called_wifi_on

    @property
    def called_wifi_off(self) -> int:
        return self._called_wifi_off

    @property
    def called_wwan_on(self) -> int:
        return self._called_wwan_on

    @property
    def called_wwan_off(self) -> int:
        return self._called_wwan_off

    def __init__(self,
                 result_call: Radio = None,
                 result_all: Radio = None,
                 result_wifi: bool = None,
                 result_wwan: bool = None,
                 raise_error: Exception = None):
        self._result_call = result_call
        self._result_all = result_all
        self._result_wifi = result_wifi
        self._result_wwan = result_wwan
        self._raise_error = raise_error
        self._called_all_on = 0
        self._called_all_off = 0
        self._called_wifi_on = 0
        self._called_wifi_off = 0
        self._called_wwan_on = 0
        self._called_wwan_off = 0

    def __call__(self) -> Radio:
        self._raise_error_if_needed()
        if not self._result_call is None:
            return self._result_call
        raise ValueError("'result_call' is not properly initialized")

    def all(self) -> Radio:
        self._raise_error_if_needed()
        if not self._result_all is None:
            return self._result_all
        raise ValueError("'result_all' is not properly initialized")

    def all_on(self) -> None:
        self._raise_error_if_needed()
        self._called_all_on += 1

    def all_off(self) -> None:
        self._raise_error_if_needed()
        self._called_all_off += 1

    def wifi(self) -> bool:
        self._raise_error_if_needed()
        if not self._result_wifi is None:
            return self._result_wifi
        raise ValueError("'result_wifi' is not properly initialized")

    def wifi_on(self) -> None:
        self._raise_error_if_needed()
        self._called_wifi_on += 1

    def wifi_off(self) -> None:
        self._raise_error_if_needed()
        self._called_wifi_off += 1

    def wwan(self) -> bool:
        self._raise_error_if_needed()
        if not self._result_wwan is None:
            return self._result_wwan
        raise ValueError("'result_wwan' is not properly initialized")

    def wwan_on(self) -> None:
        self._raise_error_if_needed()
        self._called_wwan_on += 1

    def wwan_off(self) -> None:
        self._raise_error_if_needed()
        self._called_wwan_off += 1

    def _raise_error_if_needed(self):
        if not self._raise_error is None:
            raise self._raise_error
