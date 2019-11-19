
from sys import getrecursionlimit

def swap(s: str, start: int, end: int):
    s[start], s[end] = s[end], s[start]
    return s


def permute_numbers(s: int):
    s = str(s)
    if len(s) == 0:
        return [s]

    permutations = []

    for idx, char in enumerate(s):
        temp_str = s[:idx] + s[idx + 1:]

        print(temp_str)
        rest = permute_numbers(temp_str)

        for i in range(len(rest)):
            rest[i] = char + rest[i]

        permutations = permutations + rest

    return permutations


def solve_first(n):
    found = False
    n = 0
    while not found:
        n += 1
        curr = n ** 3


if __name__ == "__main__":
    print(permute_numbers(123))
