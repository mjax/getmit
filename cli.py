#!/usr/bin/env python

from core import *
from clint import arguments
from clint.textui import colored

args = arguments.Args('status')

def main():
    if args.get(0) != None:
        if 'help' in args.get(0):
            print 'helping you'
        elif 'make' in args.get(0):
            print 'making this mit file'
        elif 'status' in args.get(0):
            print str(DATE) + " " + str(FULLNAME) 
    else:
        pass

if __name__ == '__main__':
    main()
