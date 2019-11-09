def get_primes(n):
    sieve = {}
    primes = []

    for i in range(2, n+1):
        if i not in sieve:
            sieve[i] = True
            primes.append(i)

        j = 2
        # All subsequent multiples of i are not prime.
        while i * j <= n:
            sieve[i * j] = False
            j += 1

    return primes

def solve_first(n: int):
    primes = get_primes(n)
    return sum(primes)

if __name__ == '__main__':
    print(solve_first(2000000))