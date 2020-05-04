#!/bin/python3

import math
import os
import random
import re
import sys

text_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'quarter',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

tens_dict = {
    2: 'twenty',
    3: 'thirty',
    4: 'fourty'
}

# Complete the timeInWords function below.
def timeInWords(h: int, m: int):
    hours = text_dict[h]

    minutes = str(m)

    if m == 0:
        return f'{hours} o\' clock'

    tens_text = tens_dict[int(minutes[0])]
    minutes_text = text_dict[int(minutes[1])]

    return hours + tens_text + minutes_text



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

