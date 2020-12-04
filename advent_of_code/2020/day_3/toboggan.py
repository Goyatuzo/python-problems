from typing import List

def str_to_lst(og: str) -> List[str]:
    return og.replace(' ', '').split('\n') 

def tobaggan_one(l: str) -> int:
    lst = str_to_lst(l)

    tree = 0
    i = 0
    width = len(lst[0])
    for y in range(1, len(lst)):
        # Three to the right, wrap around if over max
        i = (i + 3) % width


        if lst[y][i] == '#':
            tree += 1


    return tree