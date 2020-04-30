#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x: List[int], k: int):
    transmitters = []
    
    x.sort()

    start_pt = None
    for pt in x:
        # If there is no start point, set it as the current point
        if start_pt is None:
            start_pt = pt
        # We found a location to place
        if pt == start_pt + k:
            start_pt = None
            transmitters.append(pt)
        elif pt > start_pt + k:
            start_pt = None
            transmitters.append(pt)
            transmitters.append(start_pt)

    print(transmitters)
    return transmitters


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = len(hackerlandRadioTransmitters(x, k))

    fptr.write(str(result) + '\n')

    fptr.close()

