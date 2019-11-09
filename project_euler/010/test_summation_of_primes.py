import unittest

from summation_of_primes import solve_first


class TestSummationOfPrimes(unittest.TestCase):
    def test_given(self):
        self.assertEqual(17, solve_first(10))


if __name__ == '__main__':
    unittest.main()
