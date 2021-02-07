import re

from ._exception import UnspecifiedException
from ._system import SystemCommand, SystemCommandInterface
from .data.radio import Radio


class RadioControlInterface:

    def __call__(self) -> Radio:
        raise NotImplementedError

    def all(self) -> Radio:
        raise NotImplementedError

    def all_on(self) -> None:
        raise NotImplementedError

    def all_off(self) -> None:
        raise NotImplementedError

    def wifi(self) -> bool:
        raise NotImplementedError

    def wifi_on(self) -> None:
        raise NotImplementedError

    def wifi_off(self) -> None:
        raise NotImplementedError

    def wwan(self) -> bool:
        raise NotImplementedError

    def wwan_on(self) -> None:
        raise NotImplementedError

    def wwan_off(self) -> None:
        raise NotImplementedError


class RadioControl(RadioControlInterface):

    def __init__(self, syscmd: SystemCommandInterface = None):
        self._syscmd = syscmd or SystemCommand()

    def __call__(self) -> Radio:
        return self.all()

    def all(self) -> Radio:
        r = self._syscmd.nmcli(['radio', 'all'])
        row = r.split('\n')[1]
        m = re.search(r'^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*', row)
        if m:
            wifi_hw, wifi, wwan_hw, wwan = m.groups()
            return Radio(wifi_hw == 'enabled', wifi == 'enabled',
                         wwan_hw == 'enabled', wwan == 'enabled')
        raise UnspecifiedException(
            'Failed to parse the results of the radio command')

    def all_on(self) -> None:
        self._syscmd.nmcli(['radio', 'all', 'on'])

    def all_off(self) -> None:
        self._syscmd.nmcli(['radio', 'all', 'off'])

    def wifi(self) -> bool:
        r = self._syscmd.nmcli(['radio', 'wifi'])
        return r.replace('\n', '') == 'enabled'

    def wifi_on(self) -> None:
        self._syscmd.nmcli(['radio', 'wifi', 'on'])

    def wifi_off(self) -> None:
        self._syscmd.nmcli(['radio', 'wifi', 'off'])

    def wwan(self) -> bool:
        r = self._syscmd.nmcli(['radio', 'wwan'])
        return r.replace('\n', '') == 'enabled'

    def wwan_on(self) -> None:
        self._syscmd.nmcli(['radio', 'wwan', 'on'])

    def wwan_off(self) -> None:
        self._syscmd.nmcli(['radio', 'wwan', 'off'])
