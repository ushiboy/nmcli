from typing import List

from .._general import GeneralControlInterface
from ..data.general import General


class DummyGeneralControl(GeneralControlInterface):

    @property
    def set_hostname_args(self):
        return self._set_hostname_args

    def __init__(self,
                 result_call: General = None,
                 result_status: General = None,
                 result_hostname: str = 'localhost',
                 raise_error: Exception = None):
        self._raise_error = raise_error
        self._result_call = result_call
        self._result_status = result_status
        self._result_hostname = result_hostname
        self._set_hostname_args: List[str] = []

    def __call__(self) -> General:
        self._raise_error_if_needed()
        if not self._result_call is None:
            return self._result_call
        raise ValueError("'result_call' is not properly initialized")

    def status(self) -> General:
        self._raise_error_if_needed()
        if not self._result_status is None:
            return self._result_status
        raise ValueError("'result_status' is not properly initialized")

    def get_hostname(self) -> str:
        self._raise_error_if_needed()
        return self._result_hostname

    def set_hostname(self, hostname: str):
        self._raise_error_if_needed()
        self._set_hostname_args.append(hostname)

    def _raise_error_if_needed(self):
        if not self._raise_error is None:
            raise self._raise_error
