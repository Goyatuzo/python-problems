import unittest

from b_even_fibonacci import *

class TestTwo(unittest.TestCase):
    def test_fib_first_ten(self):
        self.assertEqual([0, 1, 1, 2, 3, 5, 8], fib(10))

    def test_given(self):
        self.assertEqual(10, solve(10))
        self.assertEqual(44, solve(100))

if __name__ == '__main__':
    unittest.main()