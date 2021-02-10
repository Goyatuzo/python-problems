import unittest

from six import Solution


class TestSix(unittest.TestCase):
    def test_basic(self):
        s = Solution()
        self.assertEqual('A', s.convert("A", 1))

    def test_one(self):
        s = Solution()
        self.assertEqual('PAHNAPLSIIGYIR', s.convert("PAYPALISHIRING", 3))

    def test_two(self):
        s = Solution()
        self.assertEqual('PINALSIGYAHRPI', s.convert("PAYPALISHIRING", 4))


if __name__ == '__main__':
    unittest.main()
