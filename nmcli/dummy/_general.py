from typing import Optional
from .._general import GeneralControlInterface
from ..data.general import General

class DummyGeneralControl(GeneralControlInterface):

    def __init__(self, result_call: Optional[General] = None,
                 raise_error: Exception = None):
        self._raise_error = raise_error
        self._result_call = result_call

    def __call__(self) -> General:
        if not self._raise_error is None:
            raise self._raise_error
        if not self._result_call is None:
            return self._result_call
        raise ValueError("'result_call' is not properly initialized")
