from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        result = []

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            a = nums1[i]
            b = nums2[j]

            if a == b:
                result.append(a)

                i += 1
                j += 1
            elif a < b:
                i += 1
            else:
                j += 1

        return result
