#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s: int, t: int, a: int, b: int, apples: List[int], oranges: List[int]):
    pass

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

