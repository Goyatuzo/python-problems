from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        current_len = n + m - 1

        print(m)
        print(n)

        while n > 0:
            a_n = nums1[m - 1]
            b_n = nums2[n - 1]

            if m <= 0 or a_n >= b_n:
                nums1[current_len] = a_n
                m -= 1
            else:
                nums1[current_len] = b_n
                n -= 1

            print(f"n: {current_len} val: {a_n} vs {b_n}, arr: {nums1}")

            current_len -= 1

#            nums1 = []
                
