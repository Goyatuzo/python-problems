
from sys import getrecursionlimit

def lex_sort(s: int):
    return ''.join(sorted(sorted(str(s))))

def permute_numbers(s: int):
    s = str(s)
    if len(s) == 0:
        return [s]

    permutations = []

    for idx, char in enumerate(s):
        temp_str = s[:idx] + s[idx + 1:]

        rest = permute_numbers(temp_str)

        for i in range(len(rest)):
            rest[i] = char + rest[i]

        permutations = permutations + rest

    return permutations


def solve_first(n):
    num = 1
    while True:
        candidate = num ** 3
        permutations = set(permute_numbers(candidate))

        count = 0
        for perm in permutations:
            if perm[0] == '0':
                continue

            cubic_root = round(int(perm) ** (1 / 3), 10)

            if cubic_root.is_integer():
                print('Number: ', str(num) + ', Permutation: ' +
                      str(perm) + ', Root: ' + str(cubic_root))
                count += 1

        if count == n:
            return num

        num += 1

def solve_second(n: int):
    # Hold the dictionaries of the cubic numbers that have come before.
    d = {}
    num = 1
    while True:
        candidate = num ** 3

        sorted_candidate = lex_sort(candidate)
        
        if sorted_candidate in d:
            d[sorted_candidate].append(num)
        else:
            d[sorted_candidate] = [num]

        if len(d[sorted_candidate]) == n:
            return d[sorted_candidate][0]

        num += 1

if __name__ == "__main__":
    print(solve_second(5))
