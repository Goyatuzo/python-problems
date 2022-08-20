from typing import List

class Solution:
    def maxSubArray(self, s: List[int]) -> bool:
        maximums = [s[0]]

        for num in s[1:]:
            curr_max = max(maximums[-1] + num, num)
            maximums.append(curr_max)

        return max(maximums)
