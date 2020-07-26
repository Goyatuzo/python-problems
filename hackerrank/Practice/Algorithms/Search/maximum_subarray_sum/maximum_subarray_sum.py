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

    for num in a:
        tmp = [num + i for i in lst]
        tmp.append(num)
        lst = tmp + lst

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

