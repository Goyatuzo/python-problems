import unittest

from sum_square_difference import *


class TestSumSquareDifference(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(2640, difference(10))


if __name__ == '__main__':
    unittest.main()
