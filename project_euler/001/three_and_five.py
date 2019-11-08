# https://www.hackerrank.com/contests/projecteuler/challenges/euler022/problem


def solve_unoptimized(n: int) -> int:
    n -= 1

    # find how many multiples of 3 there are
    three_mod = n % 3
    three_n = n - three_mod

    multiples_of_three = three_n / 3

    # Partial sum formula for 3 + 6 + n
    three_sum = int((3 / 2) * multiples_of_three * (multiples_of_three + 1))

    # find how many multiples of 5 there are
    five_mod = n % 5
    five_n = n - five_mod

    multiples_of_five = five_n / 5

    five_sum = int((5 / 2) * multiples_of_five * (multiples_of_five + 1))

    # find how many multiples of fifteen there are
    fifteen_mod = n % 15
    fifteen_n = n - fifteen_mod

    multiples_of_fifteen = fifteen_n / 15

    fifteen_sum = int((15 / 2) * multiples_of_fifteen *
                      (multiples_of_fifteen + 1))

    return three_sum + five_sum - fifteen_sum


if __name__ == '__main__':
    print(solve_unoptimized(1000))
