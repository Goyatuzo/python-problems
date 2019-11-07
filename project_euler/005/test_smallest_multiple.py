import unittest

from smallest_multiple import *

class TestSmallsetMultiple(unittest.TestCase):
    def test_given(self):
        self.assertEqual(3, solve(6))
        self.assertEqual(10, solve(2520))

if __name__ == '__main__':
    unittest.main()