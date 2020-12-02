def cut_ribbon(n: int, a: int, b: int, c: int) -> int:
    cache = [0] * (n + a + b + c)

    # Set the initial states to 1
    cache[a] = 1
    cache[b] = 1
    cache[c] = 1

    for i in range(n):
        # If the stored value is 0, then it's not part of the sequence
        if cache[i] != 0:
            cache[i + a] = max(cache[i] + 1, cache[i + a])
            cache[i + b] = max(cache[i] + 1, cache[i + b])
            cache[i + c] = max(cache[i] + 1, cache[i + c])

    return cache[n]


if __name__ == '__main__':
    n, a, b, c = list(map(int, input().split(' ')))

    print(cut_ribbon(n, a, b, c))