#!/usr/bin/env python

import os
import datetime

__title__ = 'getmit'
__author__ = 'Edgar Gavrik'
__license__ = 'MIT'

FULLNAME = 'Edgar Gavrik'
DATE = datetime.date.today().year

def read_mit():
    with open('MIT.txt', 'r') as f:
        mit = f.read()
    return mit

mit = read_mit()

def write_mit():
    os.system('touch DEMO.txt')
    with open('DEMO.txt', 'w') as f:
        make_mit = f.write(mit.format(DATE, FULLNAME))
    return '*ok'

def make_mit():
    mit = read_mit()
    return mit.format(DATE, FULLNAME)

def required():
    return 'License and copyright notice'

def permitted():
    perm = {1: 'Commercial Use', 2: 'Distribution', 3: 'Modification', 4: 'Private Use', 5: 'Sublicensing'}
    return perm

def forbidden():
    return 'Hold Liable'
