#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

# Complete the minimumLoss function below.


def minimumLoss(price: List[int]) -> int:
    min_loss = -1

    for i in range(len(price) - 2):
        # Find the max value of the valid entries
        valid_vals = [val for val in price[i + 1:] if val < price[i]]

        # If there are no valid values left, just skip
        if len(valid_vals) == 0:
            continue

        biggest = max([val for val in price[i + 1:] if val < price[i]])

        diff = price[i] - biggest

        if min_loss == -1:
            min_loss = diff
        else:
            min_loss = min(diff, min_loss)

    return min_loss


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
