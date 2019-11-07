def get_primes(n):
    sieve = {}
    primes = []

    for i in range(2, n + 1):
        if i not in sieve:
            sieve[i] = True
            primes.append(i)

        j = 2
        # All subsequent multiples of i are not prime.
        while i * j < n:
            sieve[i * j] = False
            j += 1

    return primes

def get_nth_primes(n):
    """Use this function by inputting a list of the nth prime you wish to compute.
    So for an example, if values = [1, 2], the output will be [2, 3].
    :param values: The nth prime values you wish to compute."""
    primes = get_primes(max(n) * 100) # Find the largest value to be computed and make list size fit to that.

    return [primes[i - 1] for i in n]