import unittest

from merge_sorted_array import Solution


class TestMergeSortedArray(unittest.TestCase):
    def test_one(self):
        s = Solution()
        a = [1, 2, 3, 0, 0, 0]
        b = [2, 5, 6]
        expected = [1, 2, 2, 3, 5, 6]
        s.merge(a, 3, b, 3)

        self.assertListEqual(expected, a)

    def test_two(self):
        s = Solution()
        a = [1]
        b = []
        expected = [1]
        s.merge(a, 1, b, 0)

        self.assertListEqual(expected, a)

    def test_three(self):
        s = Solution()
        a = [0]
        b = [1]
        expected = [1]
        s.merge(a, 0, b, 1)

        self.assertListEqual(expected, a)


if __name__ == '__main__':
    unittest.main()
