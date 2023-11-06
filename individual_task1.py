#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
import sys


# Using List Comprehensions for solving problem
def find_negative_composition_comprehension_version(list_a: list):
    print(reduce(lambda a, b: a * b, [el for el in list_a if el < 0]))


# Using ordinary loops for solving problem
def find_negative_composition_loop_version(list_a: list):
    composition = 1
    for num in list_a:
        if num < 0:
            composition *= num
    print(composition)


if __name__ == '__main__':
    input_list = [int(el) for el in input().split()]
    if len(input_list) != 10:
        print('Invalid list length!', file=sys.stderr)
    else:
        find_negative_composition_comprehension_version(input_list)
        find_negative_composition_loop_version(input_list)