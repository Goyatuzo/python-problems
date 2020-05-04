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

# Complete the timeInWords function below.
def timeInWords(h: int, m: int):
    # o' clock case
    if m == 0:
        hours = text_dict[h]
        return f'{hours} o\' clock'

    if m > 40:
        minutes = 60 - m

        minutes_text = text_dict[minutes]

        if m == 45:
            m_text = ''
        else:
            m_text = 'minutes '

        return f'{minutes_text} {m_text}to {text_dict[h + 1]}'
    elif m == 40:
        return f'twenty minutes to {text_dict[h + 1]}'
    elif m > 30:
        minutes = str(60 - m)

        return f'twenty {text_dict[int(minutes[1])]} minutes to {text_dict[h + 1]}'
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

