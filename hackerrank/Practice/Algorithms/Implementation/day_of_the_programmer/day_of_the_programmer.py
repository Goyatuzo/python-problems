#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def day_of_the_programmer(year):
    is_gregorian_leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100
                                                 != 0)
    is_julian_leap_year = year % 4 == 0
    

    if year > 1918:
        if is_gregorian_leap_year:
            return f"12.09.{year}"
        return f"13.09.{year}"
    elif year == 1918:
        return "26.09.1918"
    else:
        if is_julian_leap_year:
            return f"12.09.{year}"
        return f"13.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = day_of_the_programmer(year)

    fptr.write(result + '\n')

    fptr.close()
