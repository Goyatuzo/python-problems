from typing import List

def sum_aoc_sort(l: List[int], tgt: int):
    l.sort()

    return sum_aoc(l, tgt)

def sum_aoc(l: List[int], tgt: int):
    """Assuming the list is sorted, we have a pointer
    in the start and end and move one or the other each
    iteration based on the current sum."""
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

def sum_three(l: List[int], tgt: int):
    """Utilize the previous problem to achieve n^2 time.
    Since we can find the sum with two numbers in n time,
    we just fix one number and run the previous algorithm."""
    l.sort()

    for i in range(len(l)):
        sub_target = tgt - l[i] 
        sub_problem = sum_aoc(l[i:], sub_target)

        # If answer was found, return it and multiple current value.
        if sub_problem != -1:
            return sub_problem * l[i]

    return -1



if __name__ == "__main__":
    lst = []

    with open('input.txt', 'r') as f:
        line = f.readline()

        while line:
            lst.append(int(line))
            line = f.readline()

    print(f'Part 1: {sum_aoc_sort(lst, 2020)}')
    print(f'Part 2: {sum_three(lst, 2020)}')
