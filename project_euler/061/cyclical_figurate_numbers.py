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


def solve_first(n: int) -> int:
    for i in range(45, 141):
        last_two_digits = str(triangle(i))[2:4]


    return 0

if __name__ == "__main__":
    print(solve_first(6))