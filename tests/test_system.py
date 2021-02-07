# pylint: disable=line-too-long
from subprocess import CalledProcessError, CompletedProcess

import pytest

from nmcli import SystemCommand
from nmcli._exception import (ConnectionActivateFailedException,
                              ConnectionDeactivateFailedException,
                              ConnectionDeleteFailedException,
                              DisconnectDeviceFailedException,
                              InvalidUserInputException,
                              NetworkManagerNotRunningException,
                              NotExistException, ScanningNotAllowedException,
                              TimeoutExpiredException, UnspecifiedException)


class DummySubprocessRunner:

    @property
    def passed_args(self):
        return self._args

    def __init__(self, return_code=0, stdout=b'', stderr=b''):
        self._args = None
        self._return_code = return_code
        self._stdout = stdout
        self._stderr = stderr

    def __call__(self, args, capture_output, check, env):
        self._args = args
        if self._return_code == 0:
            return CompletedProcess(args, self._return_code, stdout=self._stdout)
        raise CalledProcessError(self._return_code, args, stderr=self._stderr)


def test_nmcli_when_successed():
    run = DummySubprocessRunner(stdout=b'test')
    s = SystemCommand(run)
    assert s.nmcli('connection') == 'test'
    assert run.passed_args == ['sudo', 'nmcli', 'connection']


def test_nmcli_when_successed_with_list_args():
    run = DummySubprocessRunner(stdout=b'test')
    s = SystemCommand(run)
    assert s.nmcli(['device', 'wifi']) == 'test'
    assert run.passed_args == ['sudo', 'nmcli', 'device', 'wifi']


def test_nmcli_when_failed_with_invalid_user_input():
    run = DummySubprocessRunner(return_code=2)
    s = SystemCommand(run)

    with pytest.raises(InvalidUserInputException):
        s.nmcli('connection')


def test_nmcli_when_failed_with_timeout_expired():
    run = DummySubprocessRunner(return_code=3)
    s = SystemCommand(run)

    with pytest.raises(TimeoutExpiredException):
        s.nmcli('connection')


def test_nmcli_when_failed_with_connection_activate():
    run = DummySubprocessRunner(return_code=4)
    s = SystemCommand(run)

    with pytest.raises(ConnectionActivateFailedException):
        s.nmcli('connection')


def test_nmcli_when_failed_with_connection_deactivate():
    run = DummySubprocessRunner(return_code=5)
    s = SystemCommand(run)

    with pytest.raises(ConnectionDeactivateFailedException):
        s.nmcli('connection')


def test_nmcli_when_failed_with_disconnect_device():
    run = DummySubprocessRunner(return_code=6)
    s = SystemCommand(run)

    with pytest.raises(DisconnectDeviceFailedException):
        s.nmcli('connection')


def test_nmcli_when_failed_with_connection_delete():
    run = DummySubprocessRunner(return_code=7)
    s = SystemCommand(run)

    with pytest.raises(ConnectionDeleteFailedException):
        s.nmcli('connection')


def test_nmcli_when_failed_with_network_manager_not_running():
    run = DummySubprocessRunner(return_code=8)
    s = SystemCommand(run)

    with pytest.raises(NetworkManagerNotRunningException):
        s.nmcli('connection')


def test_nmcli_when_failed_with_not_exist():
    run = DummySubprocessRunner(return_code=10)
    s = SystemCommand(run)

    with pytest.raises(NotExistException):
        s.nmcli('connection')


def test_nmcli_when_failed_with_unspecified():
    run = DummySubprocessRunner(return_code=1)
    s = SystemCommand(run)

    with pytest.raises(UnspecifiedException):
        s.nmcli('connection')


def test_nmcli_when_failed_with_scanning_not_allowed():
    run = DummySubprocessRunner(return_code=1,
                                stderr=b'Error: Scanning not allowed immediately following previous scan.')
    s = SystemCommand(run)

    with pytest.raises(ScanningNotAllowedException):
        s.nmcli('connection')


def test_disable_use_sudo():
    run = DummySubprocessRunner(stdout=b'test')
    s = SystemCommand(run)
    s.disable_use_sudo()
    assert s.nmcli('connection') == 'test'
    assert run.passed_args == ['nmcli', 'connection']
