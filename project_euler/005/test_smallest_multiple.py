import unittest

from smallest_multiple import *

class TestSmallsetMultiple(unittest.TestCase):
    def test_given(self):
        self.assertEqual(6, solve(3))
        self.assertEqual(2520, solve(10))

if __name__ == '__main__':
    unittest.main()