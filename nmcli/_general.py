from ._system import SystemCommandInterface, SystemCommand
from .data import General

class GeneralControlInterface:

    def __call__(self) -> General:
        raise NotImplementedError

    def status(self) -> General:
        raise NotImplementedError

class GeneralControl(GeneralControlInterface):

    def __init__(self, syscmd: SystemCommandInterface = None):
        self._syscmd = syscmd or SystemCommand()

    def __call__(self) -> General:
        return self.status()

    def status(self) -> General:
        r = self._syscmd.nmcli(['general', 'status'])
        return General.parse(r.split('\n')[1])
