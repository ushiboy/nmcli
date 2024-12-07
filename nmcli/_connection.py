import re
from typing import List, Optional

from ._helper import add_wait_option_if_needed
from ._system import SystemCommand, SystemCommandInterface
from .data.connection import Connection, ConnectionDetails, ConnectionOptions


class ConnectionControlInterface:

    def __call__(self) -> List[Connection]:
        raise NotImplementedError

    def add(self,
            conn_type: str,
            options: Optional[ConnectionOptions] = None,
            ifname: str = "*",
            name: str = None,
            autoconnect: bool = None) -> None:
        raise NotImplementedError

    def modify(self, name: str, options: ConnectionOptions) -> None:
        raise NotImplementedError

    def delete(self, name: str, wait: int = None) -> None:
        raise NotImplementedError

    def up(self, name: str, wait: int = None) -> None:
        raise NotImplementedError

    def down(self, name: str, wait: int = None) -> None:
        raise NotImplementedError

    def show(self, name: str, show_secrets: bool = False) -> ConnectionDetails:
        raise NotImplementedError

    def reload(self) -> None:
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
            autoconnect: bool = None) -> None:
        cmd = ['connection', 'add', 'type', conn_type, 'ifname', ifname]
        if autoconnect is not None:
            cmd += ['autoconnect', 'yes' if autoconnect else 'no']
        if not name is None:
            cmd += ['con-name', name]
        options = {} if options is None else options
        for k, v in options.items():
            cmd += [k, v]
        self._syscmd.nmcli(cmd)

    def modify(self, name: str, options: ConnectionOptions) -> None:
        cmd = ['connection', 'modify', name]
        for k, v in options.items():
            cmd += [k, v]
        self._syscmd.nmcli(cmd)

    def delete(self, name: str, wait: int = None) -> None:
        cmd = add_wait_option_if_needed(
            wait) + ['connection', 'delete', name]
        self._syscmd.nmcli(cmd)

    def up(self, name: str, wait: int = None) -> None:
        cmd = add_wait_option_if_needed(wait) + ['connection', 'up', name]
        self._syscmd.nmcli(cmd)

    def down(self, name: str, wait: int = None) -> None:
        cmd = add_wait_option_if_needed(
            wait) + ['connection', 'down', name]
        self._syscmd.nmcli(cmd)

    def show(self, name: str, show_secrets: bool = False) -> ConnectionDetails:
        cmd = ['connection', 'show', name]
        if show_secrets:
            cmd += ["--show-secrets"]
        r = self._syscmd.nmcli(cmd)
        results = {}
        for row in r.split('\n'):
            m = re.search(r'^(\S+):\s*([\S\s]+)\s*', row)
            if m:
                key, value = m.groups()
                results[key] = None if value in ('--', '""') else value
        return results

    def reload(self) -> None:
        self._syscmd.nmcli(['connection', 'reload'])
