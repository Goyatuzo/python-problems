#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.


def minimumLoss(price):
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
