from typing import List, Optional, Tuple

from .._connection import (ConnectionControlInterface, ConnectionDetails,
                           ConnectionOptions)
from ..data.connection import Connection


class DummyConnectionControl(ConnectionControlInterface):

    @property
    def add_args(self):
        return self._add_args

    @property
    def modify_args(self):
        return self._modify_args

    @property
    def delete_args(self):
        return self._delete_args

    @property
    def up_args(self):
        return self._up_args

    @property
    def down_args(self):
        return self._down_args

    @property
    def called_reload(self) -> int:
        return self._called_reload

    def __init__(self,
                 result_call: List[Connection] = None,
                 result_show: ConnectionDetails = None,
                 raise_error: Exception = None):
        self._raise_error = raise_error
        self._result_call = result_call or []
        self._result_show = result_show
        self._add_args: List[Tuple] = []
        self._modify_args: List[Tuple] = []
        self._delete_args: List[str] = []
        self._up_args: List[str] = []
        self._down_args: List[str] = []
        self._called_reload = 0

    def __call__(self) -> List[Connection]:
        self._raise_error_if_needed()
        return self._result_call

    def add(self,
            conn_type: str,
            options: Optional[ConnectionOptions] = None,
            ifname: str = "*",
            name: str = None,
            autoconnect: bool = False) -> None:
        self._raise_error_if_needed()
        self._add_args.append((conn_type, options, ifname, name, autoconnect))

    def modify(self, name: str, options: ConnectionOptions) -> None:
        self._raise_error_if_needed()
        self._modify_args.append((name, options))

    def delete(self, name: str) -> None:
        self._raise_error_if_needed()
        self._delete_args.append(name)

    def up(self, name: str) -> None:
        self._raise_error_if_needed()
        self._up_args.append(name)

    def down(self, name: str) -> None:
        self._raise_error_if_needed()
        self._down_args.append(name)

    def show(self, name: str) -> ConnectionDetails:
        self._raise_error_if_needed()
        if not self._result_show is None:
            return self._result_show
        raise ValueError("'result_show' is not properly initialized")

    def reload(self) -> None:
        self._raise_error_if_needed()
        self._called_reload += 1

    def _raise_error_if_needed(self):
        if not self._raise_error is None:
            raise self._raise_error
