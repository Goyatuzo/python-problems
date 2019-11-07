import unittest

from smallest_multiple import *

class TestSmallsetMultiple(unittest.TestCase):
    def test_given(self):
        self.assertEqual(6, solve(3))
        self.assertEqual(2520, solve(10))

    def test_extra(self):
        self.assertEqual(232792560, solve(20))

if __name__ == '__main__':
    unittest.main()