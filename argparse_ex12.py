#! /usr/bin/env python


# execute as follows:
# ./argparse_ex1.py -h
# ./argparse_ex1.py --op
# ./argparse_ex1.py --op sum
# ./argparse_ex1.py --op sum 1 2 3 Divya

import argparse

parser = argparse.ArgumentParser(description='This script will find sum or diff of a list of numbers')
parser.add_argument('--op', choices=['sum', 'sub'], required=True)
parser.add_argument('integers', type=int, nargs='+', help='List of numbers to be used by operation')

values = parser.parse_args()
print(vars(values))
print(values.op)

if values.op == 'sum':
    print(sum(values.integers))
elif values.op == 'sub':
    result = values.integers[0]

    for num in values.integers[1:]:
        result -= num
    print(result)
