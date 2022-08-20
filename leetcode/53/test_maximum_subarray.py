import unittest

from maximum_subarray import Solution


class TestMaximumSubarray(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(6, s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

    def test_2(self):
        s = Solution()
        self.assertEqual(1, s.maxSubArray([1]))

    def test_3(self):
        s = Solution()
        self.assertEqual(23, s.maxSubArray([5,4,-1,7,8]))

    def test_4(self):
        s = Solution()
        self.assertEqual(-1, s.maxSubArray([-1, -1, -1]))


if __name__ == '__main__':
    unittest.main()
