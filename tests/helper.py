from nmcli._system import SystemCommandInterface

class DummySystemCommand(SystemCommandInterface):

    @property
    def passed_parameters(self):
        return self._parameters

    def __init__(self, result='', raise_error=None):
        self._result = result
        self._raise_error = raise_error

    def nmcli(self, parameters):
        self._parameters = parameters
        if not self._raise_error is None:
            raise self._raise_error
        return self._result
