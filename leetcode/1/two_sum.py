from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        other = {}

        for count, num in enumerate(nums):
            if num in other:
                return [other[num], count]
            other[target - num] = count

        return None
