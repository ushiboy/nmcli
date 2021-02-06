from nmcli._system import SystemCommandInterface

class DummySystemCommand(SystemCommandInterface):

    @property
    def passed_parameters(self):
        return self._parameters

    def __init__(self, result=None, raise_error=None):
        result = [] if result is None else result
        if isinstance(result, str):
            result = [result]
        if not isinstance(result, list):
            raise ValueError('The result must be specified as list or str')
        self._result = result
        self._raise_error = raise_error
        self._parameters = []

    def nmcli(self, parameters):
        self._parameters = parameters
        if not self._raise_error is None:
            raise self._raise_error
        if len(self._result) > 0:
            return self._result.pop(0)
        return ''
