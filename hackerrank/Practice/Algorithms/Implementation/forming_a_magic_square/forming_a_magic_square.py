#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

def magic_square_delta(s: List[List[int]]) -> int:
    magic_square = formingMagicSquare(s)

    total = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            total += abs(s[i][j] - magic_square[i][j])

    return total

# Complete the formingMagicSquare function below.
def formingMagicSquare(s: List[List[int]]):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

