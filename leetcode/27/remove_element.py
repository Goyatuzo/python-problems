from typing import List

def remove_element(nums: List[int], val: int) -> int:
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] == val:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        else:
            count += 1


    for n in nums:
        if n != val:
            count += 1

    print(nums)

    return count
