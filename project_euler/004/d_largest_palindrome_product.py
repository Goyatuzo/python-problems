import math

def is_palindrome(value):
    value = str(value)

    # The half-way index. This should be the last digit checked.
    n = int(len(value) / 2)
    # The index of the last digit of the number.
    last_idx = len(value) - 1

    return all([value[i] == value[last_idx - i] for i in range(0, n)])

def largest_palindrome(limit):
    """Since the number's square root is technically the largest value
    we only need to iterate from 1 to the square root of the number.

    This solution is a bit different from the one that solves the question in
    the actual website. I'm using HackerRank's interface to solve the problems.
    :param limit: The highest value a palindrome can be."""

    max_palindrome = 0

    for i in range(100, 1000):
        for j in range(1, 1000):

            # The current value to be evaluated.
            value = i * j

            # If the current value is greater than limit, go to next i.
            if value > limit or j > i:
                break
            
            # Otherwise, if it's a palindrome, check to see if it's the biggest.
            if value > max_palindrome and is_palindrome(value):
                max_palindrome = value

    return max_palindrome
