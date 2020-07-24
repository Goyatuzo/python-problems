#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

# https://www.hackerrank.com/challenges/minimum-loss/problem


def find_min(lst: List[int], thresh: int) -> int:
    """Find the min in a given list and threshold. Assumes
    the input list is sorted in ascending order."""
    if len(lst) < 2:
        return lst[0]

    local_min = lst[1] - lst[0]
    min_tup = (lst[0], lst[1])

    for i in range(len(lst) - 1):
        diff = lst[i + 1] - lst[i]
        if diff > thresh and diff < local_min:
            local_min = diff
            min_tup = (lst[i], lst[i + 1])

    return min_tup


# Complete the minimumLoss function below.

def minimumLoss(price: List[int]) -> int:
    sorted_price = sorted(price)

    found = False
    iter_count = 0

    while not found:
        local_min = find_min(sorted_price, iter_count)

        # Verify the second number appears before the first
        if price.index(local_min[1]) < price.index(local_min[0]):
            return local_min[1] - local_min[0]
        else:
            iter_count = local_min[1] - local_min[0]

    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
