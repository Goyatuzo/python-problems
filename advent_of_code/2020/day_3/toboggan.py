from typing import List

def str_to_lst(og: str) -> List[str]:
    return og.replace(' ', '').split('\n') 

def tobaggan_one(l) -> int:
    if type(l) == str:
        lst = str_to_lst(l)
    else:
        lst = l

    tree = 0
    i = 0
    width = len(lst[0])
    for y in range(1, len(lst)):
        # Three to the right, wrap around if over max
        i = (i + 3) % width


        if lst[y][i] == '#':
            tree += 1


    return tree


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = f.readlines()

        # Strip out the newlines since it was messing up the number
        lines = [line.strip() for line in lines]

    print(f'Part 1: {tobaggan_one(lines)}')
