from typing import List

class Solution:
    def containsDuplicate(self, s: List[int]) -> bool:
        count = set()

        for val in s:
            if val in count:
                return True
            count.add(val)

        return False
