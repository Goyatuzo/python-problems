def cut_ribbon(n: int, a: int, b: int, c: int) -> int:
    # Create list of n length 
    cache = [0] * (n + a + b + c)

    # Initialize first values to 1
    for i in range(int(n / a)):
        idx = i * a
        cache[idx] = i
        cache[idx + b] = i + 1
        cache[idx + c] = i + 1
        cache[idx + b + c] = i + 2

    # Now for the second values
    for i in range(int(n / b)):
        idx = i * b
        cache[idx] = max(cache[idx], i)
        cache[idx + a] = max(cache[idx + a], i + 1)
        cache[idx + c] = max(cache[idx + c], i + 1)
        cache[idx + a + c] = max(cache[idx + a + c], i + 2)


    for i in range(int(n / c)):
        idx = i * c
        cache[idx] = max(cache[idx], i)
        cache[idx + a] = max(cache[idx + a], i + 1)
        cache[idx + b] = max(cache[idx + b], i + 1)
        cache[idx + a + b] = max(cache[idx + a + b], i + 2)


    return cache[n]
