from typing import List

def omkar_and_waterslide(nums: List[int]) -> int:
    ops = 0

    curr_supp_min = nums[-1]
    for num in reversed(nums):
        # If the current beam is taller, we need operations
        if curr_supp_min < num:
            ops += num - curr_supp_min
            curr_supp_min = num
        # Otherwise, we're decending down
        else:
            curr_supp_min = num

    return ops

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        print(omkar_and_waterslide(a))