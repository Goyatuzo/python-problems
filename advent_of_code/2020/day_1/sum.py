from typing import List

def sum_aoc(l: List[int], tgt: int):
    l.sort()

    # Two pointers, increment or decrement one at a time until answer is hit
    begin = 0
    end = len(l) - 1

    while begin < end:
        if l[begin] + l[end] == tgt:
            return l[begin] * l[end]
        elif l[begin] + l[end] < tgt:
            begin += 1
        else:
            end -= 1

    # If it reaches this point, no two values add to tgt
    return -1

if __name__ == "__main__":
    lst = []

    with open('input.txt', 'r') as f:
        line = f.readline()

        while line:
            lst.append(int(line))
            line = f.readline()

    print(sum_aoc(lst, 2020))
