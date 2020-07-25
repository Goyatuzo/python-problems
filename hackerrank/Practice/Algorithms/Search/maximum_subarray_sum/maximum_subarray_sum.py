#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/maximum-subarray-sum/problem

# Complete the maximumSum function below.
def maximumSum(a, m):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')
        fptr.close()

