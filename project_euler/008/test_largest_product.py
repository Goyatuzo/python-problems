import unittest

from largest_product import solve_first


class TestLargestProductInASeries(unittest.TestCase):
    def test_get_primes(self):
        self.assertEqual(5832, solve_first(4))


if __name__ == '__main__':
    unittest.main()
