#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

# https://www.hackerrank.com/challenges/pairs/problem

# Complete the pairs function below.
def pairs(k: int, arr: List[int]) -> int:
    # Store the dictionary of numbers here
    number_dict = {}
    
    # Each number is uniqe, so we don't need to do any checking
    for i in arr:
        number_dict[i] = 1

    # Keep total of number of pairs
    total = 0

    for key in number_dict:
        if key - k in number_dict:
            total += 1

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

