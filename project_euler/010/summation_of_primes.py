import sys
sys.path.append(sys.path[0] + '/../../')

from helpers.sieve import Sieve


def solve_first(n: int):
    s = Sieve()
    primes = s.primes(n, False)
    return sum(primes)


if __name__ == '__main__':
    print(solve_first(2000000))
