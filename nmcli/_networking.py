from ._const import NetworkConnectivity
from ._system import SystemCommand, SystemCommandInterface


class NetworkingControlInterface:

    def __call__(self) -> NetworkConnectivity:
        raise NotImplementedError

    def on(self) -> None:
        raise NotImplementedError

    def off(self) -> None:
        raise NotImplementedError

    def connectivity(self, check: bool = False) -> NetworkConnectivity:
        raise NotImplementedError

class NetworkingControl(NetworkingControlInterface):

    def __init__(self, syscmd: SystemCommandInterface = None):
        self._syscmd = syscmd or SystemCommand()

    def __call__(self) -> NetworkConnectivity:
        return self.connectivity()

    def on(self) -> None:
        self._syscmd.nmcli(['networking', 'on'])

    def off(self) -> None:
        self._syscmd.nmcli(['networking', 'off'])

    def connectivity(self, check: bool = False) -> NetworkConnectivity:
        cmds = ['networking', 'connectivity']
        if check:
            cmds += ['check']
        return NetworkConnectivity(self._syscmd.nmcli(cmds).replace('\n', ''))
