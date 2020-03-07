#!/usr/bin/env python3
from setuptools import setup
from setuptools.command.test import test

class PyTest(test):

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)

setup(
    name='nmcli',
    version='0.2.0',
    packages=['nmcli', 'nmcli.data', 'nmcli.dummy'],
    package_data={
        'nmcli': ['py.typed'],
    },
    test_suite='tests',
    python_requires='>=3.7',
    install_requires=[
    ],
    tests_require=[
        'pytest'
    ],
    cmdclass={'test': PyTest}
)
