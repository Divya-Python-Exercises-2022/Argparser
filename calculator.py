#! /usr/bin/env python

import sys

def sum():
    total = 0
    print(sys.argv)

    for arg in sys.argv[2:]:
        total += int(arg)
    print(total)


def sub():
    total = int(sys.argv[2])
    print(sys.argv)


    for arg in sys.argv[3:]:
        total -= int(arg)
    print(total)

if len(sys.argv) < 4:
    print('Invalid args')
elif sys.argv[1] == '--sum':
    sum()
elif sys.argv[1] == '--sub':
    sub()
