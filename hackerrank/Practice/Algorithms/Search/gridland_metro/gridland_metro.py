#!/bin/python3

import math
import os
import random
import re
import sys

from operator import itemgetter
from typing import List

# Complete the gridlandMetro function below.
def gridlandMetro(n: int, m: int, k: int, track: List[List[int]]) -> int:
    track.sort(key=itemgetter(0, 1, 2))

    unoccupied_grid = n * m

    prev_row, prev_start, prev_end = [-1, -1, -1]
    for entry in track:
        row, start, end = entry

        print(unoccupied_grid)

        if prev_row != row or start > prev_end:
            unoccupied_grid = unoccupied_grid - (end - start + 1)
        elif start <= prev_end and end > prev_end:
            unoccupied_grid = unoccupied_grid - (end - prev_end)


        prev_row, prev_start, prev_end = entry

    return unoccupied_grid

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
