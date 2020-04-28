#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s: int, t: int, a: int, b: int, apples: List[int], oranges: List[int]):
    ap = [apple for apple in apples if a + apple >= s and a + apple <= t]
    og = [orange for orange in oranges if b + orange >= s and b + orange <= t]

    return (len(ap), len(og))

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

    apple, orange = countApplesAndOranges(s, t, a, b, apples, oranges)

    print(apple)
    print(orange)
