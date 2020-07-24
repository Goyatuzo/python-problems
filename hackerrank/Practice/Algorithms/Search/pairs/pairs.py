#!/bin/python3

import math
import os
import random
import re
import sys

from typings import List

# https://www.hackerrank.com/challenges/pairs/problem

# Complete the pairs function below.
def pairs(k: int, arr: List[int]) -> int:
    number_dict = {}

    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

