from typing import List

def tobaggan_gen(lst: List[str], step: int, down: int) -> int:
    tree = 0
    i = 0
    width = len(lst[0])
    for y in range(1, len(lst), down):
        # Three to the right, wrap around if over max
        i = (i + step) % width


        if lst[y][i] == '#':
            tree += 1


    return tree



def tobaggan_one(l) -> int:
    if type(l) == str:
        lst = l.replace(' ', '').split('\n') 
    else:
        lst = l

    return tobaggan_gen(lst, 3, 1)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = f.readlines()

        # Strip out the newlines since it was messing up the number
        lines = [line.strip() for line in lines]

    print(f'Part 1: {tobaggan_one(lines)}')
