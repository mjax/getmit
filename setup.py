#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

setup(
    name='getmit',
    version='0.0.3',
    description='CLI for making MIT license',
    url='https://github.com/edgarasg/getmit',
    author='Edgar Gavrik',
    author_email='edgar.gavrik@gmail.com',
    install_requires=['clint'],
    packages=['getmit'],
    entry_points={
        'console_scripts': [
            'getmit = getmit.core:return_mit'
        ]
    }
)
