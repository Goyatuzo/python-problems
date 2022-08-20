import unittest

from two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def test_one(self):
        s = Solution()
        self.assertEqual([0, 1], s.twoSum([2, 7, 11, 15], 9))

    def test_two(self):
        s = Solution()
        self.assertEqual([1, 2], s.twoSum([3, 2, 4], 6))

    def test_three(self):
        s = Solution()
        self.assertEqual([0, 1], s.twoSum([3, 3], 6))



if __name__ == '__main__':
    unittest.main()
