from typing import List


def omkar_and_infinity_clock(k: int, nums: List[int]) -> str:
    # Find the max
    maximum = nums[0]

    for i in nums:
        maximum = i if i > maximum else maximum

    # Now keep applying it while k > 0
    while k > 0:
        nums = [maximum - ai for ai in nums]

        # Subtract 1 here since it's one operation
        k -= 1

        # Find max again
        maximum = nums[0]
        
        for i in nums:
            maximum = i if i > maximum else maximum

        
    return ' '.join(map(str, nums))