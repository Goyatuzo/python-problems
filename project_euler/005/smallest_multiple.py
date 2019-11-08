# https://www.hackerrank.com/contests/projecteuler/challenges/euler005
from typing import List
from math import sqrt, log, floor

class Sieve:
    array = []

    def generate_sieve(self, num: int):
        # Since arrays start from 0
        num = num + 1

        if len(self.array) < num:
            self.array = [True] * (num)

            for i in range(2, num + 1):
                j = 2

                while i * j - 1 < num:
                    self.array[i * j - 1] = False
                    j += 1

    def primes(self, upto: int) -> List[int]:
        self.generate_sieve(upto)
        return [idx + 1 for idx, i in enumerate(self.array) if i]

    def isPrime(self, num: int) -> bool:
        self.generate_sieve(num)
        return self.array[num]


def solve(n: int) -> int:
    s = Sieve()
    s.generate_sieve(n)

    result = 1
    
    for prime in s.primes(n):
        if prime <= 1:
            continue

        exp = floor(log(n) / log(prime))
        result *= prime ** exp
    
    return result

if __name__ == '__main__':
    print(solve(20))