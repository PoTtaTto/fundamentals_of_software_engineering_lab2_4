#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    list_ = [float(num) for num in input().split()]
    if not list_:  # Checking list is not empty
        print('List is empty!', file=sys.stderr)
    else:
        neg_i = []  # List with indexes of first 2 negative elements
        min_val, min_i = list_[0], 0
        for i, num in enumerate(list_):
            if num < min_val:  # Searching min value and it's index
                min_val, min_i = num, i
            if len(neg_i) != 2 and num < 0:  # Appending indexes of first 2 negative elements
                neg_i.append(i)
        print('Min element index:', min_i)
        print('Sum between first 2 negative elements:', sum(list_[neg_i[0]+1:neg_i[1]]) if len(neg_i) == 2 else 'None')
        print('List with abs(elements) < 1 into the beginning:', sorted(list_, key=lambda a: abs(a) > 1))

