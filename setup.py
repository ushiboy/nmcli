#!/usr/bin/env python3
from setuptools import setup
from setuptools.command.test import test

class PyTest(test):

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='nmcli',
    version='0.6.1',
    author='ushiboy',
    license='MIT',
    description='A python wrapper library for the network-manager cli client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ushiboy/nmcli',
    packages=['nmcli', 'nmcli.data', 'nmcli.dummy'],
    package_data={
        'nmcli': ['py.typed'],
    },
    test_suite='tests',
    python_requires='>=3.7',
    tests_require=[
        'pytest'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux'
    ],
    cmdclass={'test': PyTest}
)
