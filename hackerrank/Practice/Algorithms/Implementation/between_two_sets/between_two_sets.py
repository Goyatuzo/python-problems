#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List
from itertools import zip_longest
from math import sqrt

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a: List[int], b: List[int]):
    candidates = range(min(a), int(max(b)) + 1)

    valid = validate_answers(candidates, a, b)

    print(valid)
    return valid

def validate_answers(candidates: List[int], a: List[int], b: List[int]):
    answers = []

    for candidate in candidates:
        invalid = False
        for a_i, b_i in zip_longest(a, b):
            if a_i is not None and candidate % a_i != 0:
                invalid = True
                break
            if b_i is not None and b_i % candidate != 0:
                invalid = True
                break

        if not invalid:
            answers.append(candidate)

    return set(answers)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = len(getTotalX(arr, brr))

    fptr.write(str(total) + '\n')

    fptr.close()

