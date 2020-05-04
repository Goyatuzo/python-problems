#!/bin/python3

import math
import os
import random
import re
import sys

def next_chain(n: int) -> int:
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def longest_collatz(n: int) -> int:
    maximum = 0
    maximum_num = 0
    for i in range(1, n + 1):
        l = 1
        curr = i

        while curr != 1:
            curr = next_chain(curr)
            l += 1

        if l >= maximum:
            maximum_num = i
            maximum = l

        print(f'i: {i}, max: {maximum_num}, length of i: {l}')

    return maximum_num


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        print(longest_collatz(int(input())))

