from ._system import SystemCommandInterface, SystemCommand

class NetworkingControlInterface:

    def __call__(self) -> str:
        raise NotImplementedError

    def on(self) -> None:
        raise NotImplementedError

    def off(self) -> None:
        raise NotImplementedError

    def connectivity(self, check: bool = False) -> str:
        raise NotImplementedError

class NetworkingControl(NetworkingControlInterface):

    def __init__(self, syscmd: SystemCommandInterface = None):
        self._syscmd = syscmd or SystemCommand()

    def __call__(self) -> str:
        return self.connectivity()

    def on(self) -> None:
        self._syscmd.nmcli(['networking', 'on'])

    def off(self) -> None:
        self._syscmd.nmcli(['networking', 'off'])

    def connectivity(self, check: bool = False) -> str:
        cmds = ['networking', 'connectivity']
        if check:
            cmds += ['check']
        return self._syscmd.nmcli(cmds).replace('\n', '')
