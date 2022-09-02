#! /usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='This script will find sum or diff of a list of numbers')
#group = parser.add_mutually_exclusive_group(required = True)
#group.add_argument('--sum', action='store_true', help='This will add the list of numbers')
#group.add_argument('--sub', action='store_true', help='This will subtract the list of numbers')
parser.add_argument('--sum', help='Add the values')
parser.add_argument('--sub', help='Sub the values')
parser.add_argument('integers', type=int, nargs='+', help='List of numbers to be used by operation')

values = parser.parse_args()
print(vars(values))
print(values.integers)

if values.sum:
    print(sum(values.integers[1:]))
elif values.sub:
    result = values.integers[0]

    for num in values.integers[2:]:
        result -= num
    print(result)

