import math

def solve(n):
    """If you keep greedily looking for a number to divide n, starting
    from 3, the final value will be prime. Note that the number searching
    should stop at the square root of n, or else it'll be very bad for large n.
    :param n: The value to find the largest prime factor."""

    # If it's an even number, keep dividing.
    while n % 2 == 0:
        n /= 2

    if n == 1:
        return 1

    divisor = 3

    while (divisor != n):
        # If n is able to be divided, reset.
        if n % divisor == 0:
            n /= divisor
            divisor = 3
            continue

        if divisor >= math.sqrt(n):
            break

        divisor += 1

    return n