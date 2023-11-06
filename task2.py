#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    list_a = list(map(int, input().split()))  # List input
    if not list_a:  # Checking list is not empty
        print('List is empty!', file=sys.stderr)
        exit(1)

    # Searching indexes of min and max elements of list
    a_min = a_max = list_a[0]
    i_min = i_max = 0
    for i, item in enumerate(list_a):
        if item < a_min:
            i_min, a_min = i, item
        if item > a_max:
            i_max, a_max = i, item

    # Checking indexes order
    if i_min > i_max:
        i_min, i_max = i_max, i_min

    # Counting positive elements
    count = 0
    for item in list_a[i_min+1:i_max]:
        if item > 0:
            count += 1
    print(count)