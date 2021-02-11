import unittest

from answer import Solution


class TestThirteen(unittest.TestCase):
    def test_basic(self):
        s = Solution()
        self.assertEqual(3, s.romanToInt("III"))

    def test_iv(self):
        s = Solution()
        self.assertEqual(4, s.romanToInt("IV"))

    def test_lviii(self):
        s = Solution()
        self.assertEqual(58, s.romanToInt("LVIII"))




if __name__ == '__main__':
    unittest.main()
