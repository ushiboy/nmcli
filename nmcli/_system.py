import os
from subprocess import CalledProcessError, run
from typing import List, Union

from ._exception import (ConnectionActivateFailedException,
                         ConnectionDeactivateFailedException,
                         ConnectionDeleteFailedException,
                         DisconnectDeviceFailedException,
                         InvalidUserInputException,
                         NetworkManagerNotRunningException, NotExistException,
                         ScanningNotAllowedException, TimeoutExpiredException,
                         UnspecifiedException)

CommandParameter = Union[str, List[str]]


class SystemCommandInterface:

    def nmcli(self, parameters: CommandParameter) -> str:
        raise NotImplementedError

    def disable_use_sudo(self):
        raise NotImplementedError

    def set_lang(self, lang: str):
        raise NotImplementedError


class SystemCommand(SystemCommandInterface):

    def __init__(self, subprocess_run=run):
        self._run = subprocess_run
        self._use_sudo = True
        self._lang = 'C'

    def nmcli(self, parameters: CommandParameter) -> str:
        if isinstance(parameters, str):
            parameters = [parameters]
        c = ['sudo', 'nmcli'] if self._use_sudo else ['nmcli']
        commands = c + parameters
        try:
            env = dict(os.environ, **{'LANG': self._lang})
            r = self._run(commands, capture_output=True,
                          check=True, env=env)
            return r.stdout.decode('utf-8')
        except CalledProcessError as e:
            rc = e.returncode
            stderr = e.stderr.decode('utf-8')
            if rc == 2:
                raise InvalidUserInputException(
                    'Invalid user input, wrong nmcli invocation') from e
            elif rc == 3:
                raise TimeoutExpiredException('Timeout expired') from e
            elif rc == 4:
                raise ConnectionActivateFailedException(
                    'Connection activation failed') from e
            elif rc == 5:
                raise ConnectionDeactivateFailedException(
                    'Connection deactivation failed') from e
            elif rc == 6:
                raise DisconnectDeviceFailedException(
                    'Disconnecting device failed') from e
            elif rc == 7:
                raise ConnectionDeleteFailedException(
                    'Connection deletion failed') from e
            elif rc == 8:
                raise NetworkManagerNotRunningException(
                    'NetworkManager is not running') from e
            elif rc == 10:
                raise NotExistException(
                    'Connection, device, or access point does not exist') from e
            else:
                if rc == 1 and stderr.find('Scanning not allowed') > 0:
                    raise ScanningNotAllowedException(stderr) from e
                raise UnspecifiedException(
                    f'Unknown or unspecified error [code:{rc}, detail:{stderr}]') from e

    def disable_use_sudo(self):
        self._use_sudo = False

    def set_lang(self, lang: str):
        self._lang = lang
