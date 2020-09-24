from typing import List, Dict, Optional
import re
from ._system import SystemCommandInterface, SystemCommand
from .data.connection import Connection

ConnectionDetails = Dict[str, Optional[str]]
ConnectionOptions = Dict[str, str]

class ConnectionControlInterface:

    def __call__(self) -> List[Connection]:
        raise NotImplementedError

    def add(self,
            conn_type: str,
            options: Optional[ConnectionOptions] = None,
            ifname: str = "*",
            name: str = None,
            autoconnect: bool = False) -> None:
        raise NotImplementedError

    def modify(self, name: str, options: ConnectionOptions) -> None:
        raise NotImplementedError

    def delete(self, name: str) -> None:
        raise NotImplementedError

    def up(self, name: str) -> None:
        raise NotImplementedError

    def down(self, name: str) -> None:
        raise NotImplementedError

    def show(self, name: str) -> ConnectionDetails:
        raise NotImplementedError

class ConnectionControl(ConnectionControlInterface):

    def __init__(self, syscmd: SystemCommandInterface = None):
        self._syscmd = syscmd or SystemCommand()

    def __call__(self) -> List[Connection]:
        r = self._syscmd.nmcli('connection')
        results = []
        for row in r.split('\n')[1:]:
            if len(row) == 0:
                continue
            results.append(Connection.parse(row))
        return results

    def add(self,
            conn_type: str,
            options: Optional[ConnectionOptions] = None,
            ifname: str = "*",
            name: str = None,
            autoconnect: bool = False) -> None:
        params = ['connection', 'add', 'type', conn_type, 'ifname', ifname]
        if not name is None:
            params += ['con-name', name]
        options = {} if options is None else options
        for k, v in options.items():
            params += [k, v]
        self._syscmd.nmcli(params)

    def modify(self, name: str, options: ConnectionOptions) -> None:
        params = ['connection', 'modify', name]
        for k, v in options.items():
            params += [k, v]
        self._syscmd.nmcli(params)

    def delete(self, name: str) -> None:
        self._syscmd.nmcli(['connection', 'delete', name])

    def up(self, name: str) -> None:
        self._syscmd.nmcli(['connection', 'up', name])

    def down(self, name: str) -> None:
        self._syscmd.nmcli(['connection', 'down', name])

    def show(self, name: str) -> ConnectionDetails:
        r = self._syscmd.nmcli(['connection', 'show', name])
        results = {}
        for row in r.split('\n'):
            m = re.search(r'^(\S+):\s*([\S\s]+)\s*', row)
            if m:
                key, value = m.groups()
                results[key] = None if value in ('--', '""') else value
        return results
