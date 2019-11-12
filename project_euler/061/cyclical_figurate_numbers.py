from typing import Callable

def triangle(n: int) -> int:
    """Triangle 45 < n < 140"""
    return int(n * (n + 1) / 2)


def square(n: int) -> int:
    """Square 32 < n < 99"""
    return int(n ** 2)


def pentagonal(n: int) -> int:
    """Pentagonal 26 < n < 81"""
    return int(n * (3 * n - 1) / 2)


def hexagonal(n: int) -> int:
    """Hexagonal 23 < n < 70"""
    return int(n * (2 * n - 1))


def heptagonal(n: int) -> int:
    """Heptagonal 20 < n < 63"""
    return int(n * (5 * n - 3) / 2)


def octagonal(n: int) -> int:
    """Octagonal 18 < n < 58"""
    return int(n * (3 * n - 2))

def create_dict(range_limits: (int, int), method: Callable[[int], int]) -> dict:
    res_dict = {}

    for i in range(range_limits[0], range_limits[1] + 1):
        res = method(i)
        dict_key = str(res)[0:2]

        if dict_key in res_dict:
            res_dict[dict_key].append(res)
        else:
            res_dict[dict_key] = [res]

    return res_dict

def solve_first(n: int) -> int:
    square_dict = create_dict((32, 99), square)
    penta_dict = create_dict((26, 81), pentagonal)
    hexa_dict = create_dict((23, 70), hexagonal)
    hepta_dict = create_dict((20, 63), heptagonal)
    octa_dict = create_dict((18, 58), octagonal)

    # Iterate through triangle to find appropriate answers
    for i in range(45, 141):
        last_two_digits = str(triangle(i))[2:4]

        if last_two_digits not in square_dict:
            continue

        square_last_two = str(square_dict[last_two_digits])[2:4]

        if square_last_two not in penta_dict:
            continue




    return 0

if __name__ == "__main__":
    print(solve_first(6))