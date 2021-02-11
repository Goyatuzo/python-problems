import unittest

from answer import Solution


class TestAnswer(unittest.TestCase):
    def test_basic(self):
        s = Solution()
        self.assertEqual([[-1, 0, 1], [-1, -1, 2]],
                         s.threeSum([-1, 0, 1, 2, -1, -4]))


if __name__ == '__main__':
    unittest.main()
