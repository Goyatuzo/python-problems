from typing import List

class Sieve:
    array = []

    def generate_sieve(self, num: int):

        if len(self.array) < num:
            self.array = [True] * (num)

            for i in range(2, num + 1):
                j = 2

                while i * j - 1 < num:
                    self.array[i * j - 1] = False
                    j += 1

    def primes(self, upto: int, inclusive: bool = True) -> List[int]:
        if inclusive:
            self.generate_sieve(upto + 1)
        else:
            self.generate_sieve(upto)
        return [idx + 1 for idx, i in enumerate(self.array) if i][1:]

    def isPrime(self, num: int) -> bool:
        self.generate_sieve(num)
        return self.array[num]