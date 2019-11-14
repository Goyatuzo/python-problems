from typing import Callable, List, Tuple
from copy import deepcopy


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
    """Heptagonal 21 < n < 63"""
    return int(n * (5 * n - 3) / 2)


def octagonal(n: int) -> int:
    """Octagonal 19 < n < 58"""
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


def rec_search(lst: List[int], rem: List[dict], depth: int) -> List[int]:
    if depth <= 0:
        last_two = str(lst[-1])[2:4]
        first_two = str(lst[0])[0:2]

        if last_two == first_two:
            return lst

        return None

    last_two_digits = str(lst[-1])[2:4]
    # We don't need to pass in the functions because they've already been calculated in the dict
    matches = [(idx, i[last_two_digits])
               for idx, i in enumerate(rem) if last_two_digits in i]

    if len(matches) == 0:
        return None

    for match in matches:
        temp_rem = [i for idx, i in enumerate(rem) if idx != match[0]]

        for val in match[1]:
            temp_val = deepcopy(lst)
            temp_val.append(val)

            rest = rec_search(temp_val, temp_rem, depth - 1)

            if rest is None:
                continue

            return rest


def solve_first(n: int) -> int:
    square_dict = create_dict((32, 99), square)
    penta_dict = create_dict((26, 81), pentagonal)
    hexa_dict = create_dict((23, 70), hexagonal)
    hepta_dict = create_dict((21, 63), heptagonal)
    octa_dict = create_dict((19, 58), octagonal)

    # Iterate through triangle to find appropriate answers
    for i in range(45, 141):
        res = rec_search(
            [triangle(i)], [square_dict, penta_dict, hexa_dict, hepta_dict, octa_dict], n - 1)

        if res is not None:
            return res

    return []


if __name__ == "__main__":
    print(sum(solve_first(6)))
