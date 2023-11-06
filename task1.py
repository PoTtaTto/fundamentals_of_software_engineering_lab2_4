#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    list_a = list(map(int, input().split()))  # List input
    if len(list_a) != 10:  # Checking list size
        print('Wrong list size!', file=sys.stderr)
        exit(1)

    # Searching sum of absolute elements < 5
    sum_ = 0
    for num in list_a:
        if abs(num) < 5:
            sum_ += num
    # Or we can use construction sum_ = sum([el for el in list_a if abs(el) < 5])
    print(sum_)