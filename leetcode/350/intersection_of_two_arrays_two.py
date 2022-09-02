from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = {}

        for num in nums1:
            counter[num] = True

        counter_two = {}

        for num in nums2:
            counter_two[num] = True

        return [key for key in counter.keys() if key in counter_two]
