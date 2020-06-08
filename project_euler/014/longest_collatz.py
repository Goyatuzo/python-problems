#!/bin/python3

import math
import os
import random
import re
import sys

cache = {
    1: 1
}

def next_chain(n: int) -> int:
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1

def longest_collatz(n: int) -> int:
    maximum = 0
    maximum_num = 0
    for i in range(2, n + 1):
        l = 0
        curr = i
        chain = []

        while curr != 1:
            chain.append(curr)

            if curr in cache:
                l += cache[curr]
                break
            else:
                curr = next_chain(curr)
                l += 1
    
        if chain[-1] in cache:
            length = cache[chain[-1]]
        else:
            length = 1

        for val in chain[::-1]:
            cache[int(val)] = length
            length += 1

        if l >= maximum:
            maximum_num = i
            maximum = l


        # print(f'i: {i}, max: {maximum_num}, length of i: {l}')

    return maximum_num


if __name__ == '__main__':
    print(longest_collatz(1000000))
