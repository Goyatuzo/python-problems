from typing import List

def remove_element(nums: List[int], val: int) -> int:
    end = len(nums) - 1
    for i in range(len(nums)):
        if nums[i] == val:
            while end > i and nums[end] == val:
                end -= 1

            nums[i], nums[end] = nums[end], nums[i]


    count = 0

    for n in nums:
        if val == n:
            count += 1

    return len(nums) - count
