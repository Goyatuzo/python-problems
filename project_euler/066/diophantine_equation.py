from math import sqrt

def valid_d(max_d: int):
    return [d for d in range(max_d + 1) if not sqrt(d).is_integer()]

def solve_first(max_d: int):
    print(valid_d(max_d))
    return 0