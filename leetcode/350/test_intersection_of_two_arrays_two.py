import unittest

from interection_of_two_arrays import Solution


class TestIntersectionOfTwoArraysTwo(unittest.TestCase):
    def test_ex_one(self):
        s = Solution()
        self.assertEqual([2, 2], s.intersect([1, 2, 2, 1], [2, 2]))

    def test_ex_two(self):
        s = Solution()
        self.assertEqual([4, 9], s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))


if __name__ == '__main__':
    unittest.main()
