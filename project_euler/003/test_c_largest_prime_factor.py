import unittest

from c_largest_prime_factor import *

class TestLargestPrimeFactor(unittest.TestCase):

    def test_problem_statement(self):
        self.assertEqual(29, solve(13195))

    def test_given(self):
        self.assertEqual(5, solve(10))
        self.assertEqual(17, solve(17))

    def test_one(self):
        self.assertEqual(1, solve(1))

if __name__ == '__main__':
    unittest.main()