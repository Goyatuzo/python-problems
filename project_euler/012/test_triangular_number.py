import unittest

from triangular_number import solve_first


class TestHighlyDivisibleTriangularNumber(unittest.TestCase):
    def test_given(self):
        self.assertEqual(28, solve_first(5))


if __name__ == '__main__':
    unittest.main()
