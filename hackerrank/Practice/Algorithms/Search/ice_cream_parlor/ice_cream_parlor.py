#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

# Complete the icecreamParlor function below.
def icecreamParlor(m: int, arr: List[int]) -> List[int]:
    sorted_arr = sorted(arr)

    i, j = 0, len(sorted_arr) - 1

    first, second = 0, 0

    while i != j:
        if sorted_arr[i] + sorted_arr[j] == m:
            first = sorted_arr[i]
            second = sorted_arr[j]
            break
        elif sorted_arr[i] + sorted_arr[j] > m:
            j -= 1
        else:
            i += 1

    idx_i, idx_j = -1, -1

    for (idx, i) in enumerate(arr):
        if i == first and idx_i == -1:
            idx_i = idx
        elif i == second and idx_j == -1:
            idx_j = idx

    return [idx_i + 1, idx_j + 1] if idx_i < idx_j else [idx_j + 1, idx_i + 1]




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
