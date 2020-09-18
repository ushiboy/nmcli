import re
from ._exception import UnspecifiedException
from ._system import SystemCommandInterface, SystemCommand
from .data import General


class GeneralControlInterface:

    def __call__(self) -> General:
        raise NotImplementedError


class GeneralControl(GeneralControlInterface):

    def __init__(self, syscmd: SystemCommandInterface = None):
        self._syscmd = syscmd or SystemCommand()

    def __call__(self) -> General:
        r = self._syscmd.nmcli('general')
        row = r.split('\n')[1]
        m = re.search(
            r'^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*', row)
        if m:
            state, connectivity, wifi_hw, wifi, wwan_hw, wwan = m.groups()
            return General(state, connectivity, wifi_hw, wifi, wwan_hw, wwan)
        raise UnspecifiedException('Failed to parse the results of the general command')
