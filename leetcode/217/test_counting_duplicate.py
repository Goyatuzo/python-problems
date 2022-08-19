import unittest

from answer import Solution


class TestContainsDuplicate(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(True, s.containsDuplicate([1, 2, 3, 1]))

    def test_2(self):
        s = Solution()
        self.assertEqual(False, s.containsDuplicate([1, 2, 3, 4]))

    def test_3(self):
        s = Solution()
        self.assertEqual(True, s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4,
                                                    2]))


if __name__ == '__main__':
    unittest.main()
