from typing import List
from .._networking import NetworkingControlInterface
from .._const import NetworkConnectivity

class DummyNetworkingControl(NetworkingControlInterface):

    @property
    def called_on(self) -> int:
        return self._called_on

    @property
    def called_off(self) -> int:
        return self._called_off

    @property
    def connectivity_args(self) -> List[bool]:
        return self._connectivity_args

    def __init__(self,
                 result_call: NetworkConnectivity = None,
                 result_connectivity: NetworkConnectivity = None,
                 raise_error: Exception = None):
        self._result_call = result_call
        self._result_connectivity = result_connectivity
        self._raise_error = raise_error
        self._called_on = 0
        self._called_off = 0
        self._connectivity_args: List[bool] = []

    def __call__(self) -> NetworkConnectivity:
        self._raise_error_if_needed()
        if not self._result_call is None:
            return self._result_call
        raise ValueError("'result_call' is not properly initialized")

    def on(self) -> None:
        self._raise_error_if_needed()
        self._called_on += 1

    def off(self) -> None:
        self._raise_error_if_needed()
        self._called_off += 1

    def connectivity(self, check: bool = False) -> NetworkConnectivity:
        self._raise_error_if_needed()
        self._connectivity_args.append(check)
        if not self._result_connectivity is None:
            return self._result_connectivity
        raise ValueError("'result_connectivity' is not properly initialized")

    def _raise_error_if_needed(self):
        if not self._raise_error is None:
            raise self._raise_error
