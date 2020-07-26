#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/maximum-subarray-sum/problem

from typing import List

# Complete the maximumSum function below.
def maximumSum(a: List[int], m: int):
    """Keep a main list that contains all the subsets upto the nth element."""
    lst = []

    # so that we can accept the first element
    prev_l = 0

    for num in a:
        tmp = [num + i for idx, i in enumerate(lst) if idx < prev_l]
        tmp.append(num)

        prev_l = len(tmp)
        print(f'tmp: {tmp}, apd: {tmp + lst}, tmp_l: {prev_l}')
        lst = tmp + lst

    n = len(a)

    print(lst)
    assert len(lst) == n * (n + 1) / 2

    return max([x % m for x in lst])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')
        fptr.close()

