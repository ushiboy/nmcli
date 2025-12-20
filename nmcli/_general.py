from typing import List, Optional

from ._system import SystemCommand, SystemCommandInterface
from .data import General


class GeneralControlInterface:

    def __call__(self) -> General:
        raise NotImplementedError

    def status(self) -> General:
        raise NotImplementedError

    def get_hostname(self) -> str:
        raise NotImplementedError

    def set_hostname(self, hostname: str):
        raise NotImplementedError

    def reload(self, flags: Optional[List[str]] = None) -> None:
        raise NotImplementedError


class GeneralControl(GeneralControlInterface):

    VALID_RELOAD_FLAGS = ['conf', 'dns-rc', 'dns-full']

    def __init__(self, syscmd: SystemCommandInterface = None):
        self._syscmd = syscmd or SystemCommand()

    def __call__(self) -> General:
        return self.status()

    def status(self) -> General:
        r = self._syscmd.nmcli(['general', 'status'])
        return General.parse(r.split('\n')[1])

    def get_hostname(self) -> str:
        r = self._syscmd.nmcli(['general', 'hostname'])
        return r.replace('\n', '')

    def set_hostname(self, hostname: str):
        self._syscmd.nmcli(['general', 'hostname', hostname])

    def reload(self, flags: Optional[List[str]] = None) -> None:
        if flags is not None:
            for flag in flags:
                if flag not in self.VALID_RELOAD_FLAGS:
                    raise ValueError(
                        f"Invalid reload flag '{flag}'. "
                        f"Valid flags are: {', '.join(self.VALID_RELOAD_FLAGS)}"
                    )
        cmd = ['general', 'reload']
        if flags:
            cmd += flags
        self._syscmd.nmcli(cmd)
