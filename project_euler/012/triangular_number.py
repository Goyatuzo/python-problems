from math import sqrt, floor


def solve_first(n: int) -> int:
    natural_sum = 0
    curr = 0

    count = 0

    # While there are less than the required divisors
    while count < n:
        # Add current value to the total
        natural_sum += curr

        highest = floor(sqrt(natural_sum))
        count = 0
        for i in range(1, highest + 1):
            if (natural_sum / i).is_integer():
                count += 2

        # Ready next iteration
        curr += 1

    return natural_sum


if __name__ == '__main__':
    print(solve_first(500))
