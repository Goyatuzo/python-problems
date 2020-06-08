#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List, Tuple

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x: List[int], k: int):
    transmitters = [] 
    x.sort()
    
    i = 0

    while i < len(x):
        target_location = x[i] + k

        while i < len(x) and x[i] <= target_location:
            i += 1

        # Found the center
        i -= 1
        transmitters.append(x[i])
        target_location = x[i] + k

        # Go to the right edge
        while i < len(x) and x[i] <= target_location:
            i += 1

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

