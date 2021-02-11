from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        # Base case if the list doesn't have enough elements
        if nums_len < 3:
            return []

        triplets = set()
        cs = {}

        for i in range(nums_len):
            total = -nums[i]
            cs[total] = i

        for a in range(nums_len):
            for b in range(a+1, nums_len):
                if (nums[a]+nums[b]) in cs:
                    c = nums[a]+nums[b]
                    c_i = cs[nums[a]+nums[b]]

                    c = -c

                    if c_i != a and c_i != b:
                        items = tuple(sorted([nums[a], nums[b], nums[c_i]]))
                        triplets.add(items)

        return [[tup[0], tup[1], tup[2]] for tup in triplets]
