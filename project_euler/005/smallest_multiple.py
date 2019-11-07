# https://www.hackerrank.com/contests/projecteuler/challenges/euler005

class Sieve:
    array = []

    def isPrime(self, num: int) -> bool:
        if num > len(self.array):
            self.array = [True] * (num + 1)

            for i in range(4, num):
                max_diff = int(num / i)

                print(max_diff)

                for j in range(1, max_diff):
                    self.array[i * j] = False

        return self.array[num]


def solve(n: int) -> int:
    r = list(range(1, n + 1))

    s = Sieve()

    s.isPrime(r[-1])