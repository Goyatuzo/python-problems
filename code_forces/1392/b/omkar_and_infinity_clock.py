from typing import List


def omkar_and_infinity_clock(k: int, nums: List[int]) -> str:
    # There are only two patterns that interleave
    maximum = max(nums)
    # If k is odd, it's easy
    if k % 2 == 1:
        return ' '.join([str(maximum - i) for i in nums])
    else:
        nums = [maximum - i for i in nums]
        maximum = max(nums)
        return ' ' .join([str(maximum - i) for i in nums])


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())

        a = list(map(int, input().split()))

        print(omkar_and_infinity_clock(k, a))
