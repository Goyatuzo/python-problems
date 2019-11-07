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

def sum_primes(n):
    n = map(int, n)

    max_prime = max(n)

    primes = get_primes(max_prime)

    sums = []

    for i in n:
        sums.append(sum([j for j in primes if i >= j]))

    return sums