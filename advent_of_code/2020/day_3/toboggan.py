from typing import List
from pathlib import Path
from os import path

def tobaggan_gen(lst: List[str], step: int, down: int) -> int:
    tree = 0
    i = 0
    width = len(lst[0])
    for y in range(down, len(lst), down):
        # Three to the right, wrap around if over max
        i = (i + step) % width


        if lst[y][i] == '#':
            tree += 1


    return tree

def get_file(fname: str) -> List[str]:
    with open(path.join(Path(__file__).parent, fname), 'r') as f:
        lines = f.readlines()

        # Strip out the newlines since it was messing up the number
        return [line.strip() for line in lines]



def tobaggan_one(fname: str) -> int:
    lst = get_file(fname)
    return tobaggan_gen(lst, 3, 1)

def tobaggan_two(fname: str) -> int:
    lst = get_file(fname)
    return tobaggan_gen(lst, 1, 1) * \
            tobaggan_gen(lst, 3, 1) * \
            tobaggan_gen(lst, 5, 1) * \
            tobaggan_gen(lst, 7, 1) * \
            tobaggan_gen(lst, 1, 2)


if __name__ == "__main__":
    print(f'Part 1: {tobaggan_one("input.txt")}')
    print(f'Part 2: {tobaggan_two("input.txt")}')