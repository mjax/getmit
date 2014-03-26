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

def get_mit():
    os.system('touch DEMO.txt')
    with open('DEMO.txt', 'w') as f:
        make_mit = f.write(mit)
    return 'ok'

def main():
    get_mit()

if __name__ == '__main__':
    main()
