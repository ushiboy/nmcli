from ._exception import UnspecifiedException, \
        InvalidUserInputException, \
        TimeoutExpiredException, \
        ConnectionActivateFailedException, \
        ConnectionDeactivateFailedException, \
        DisconnectDeviceFailedException, \
        ConnectionDeleteFailedException, \
        NetworkManagerNotRunningException, \
        NotExistException
from subprocess import run, CalledProcessError
from typing import Union, List

CommandParameter = Union[str, List[str]]

class SystemCommandInterface(object):

    def nmcli(self, parameters: CommandParameter) -> str:
        raise NotImplementedError

class SystemCommand(SystemCommandInterface):

    def __init__(self, subprocess_run=run):
        self._run = subprocess_run

    def nmcli(self, parameters: CommandParameter) -> str:
        if isinstance(parameters, str):
            parameters = [parameters]
        commands = ['sudo', 'nmcli'] + parameters
        try:
            r = self._run(commands, capture_output=True, check=True, env={'LANG':'C'})
            return r.stdout.decode('utf-8')
        except CalledProcessError as e:
            rc = e.returncode
            if rc == 2:
                raise InvalidUserInputException
            elif rc == 3:
                raise TimeoutExpiredException
            elif rc == 4:
                raise ConnectionActivateFailedException
            elif rc == 5:
                raise ConnectionDeactivateFailedException
            elif rc == 6:
                raise DisconnectDeviceFailedException
            elif rc == 7:
                raise ConnectionDeleteFailedException
            elif rc == 8:
                raise NetworkManagerNotRunningException
            elif rc == 10:
                raise NotExistException
            else:
                raise UnspecifiedException
