#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

# Complete the gridlandMetro function below.
def gridlandMetro(n: int, m: int, k: int, track: List[List[int]]) -> int:
    grid = [[0 for i in range(n)] for j in range(m)]

    for entry in track:
        row = entry[0] - 1
        start = entry[1] - 1
        end = entry[2] - 1


        for i in range(start, end + 1):
            grid[row][i] = 1


    return [val for entry in grid for val in entry].count(0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
