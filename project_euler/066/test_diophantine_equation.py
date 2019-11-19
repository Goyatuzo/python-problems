import unittest

from diophantine_equation import solve_first, valid_d


class TestDiophantineEquation(unittest.TestCase):
    def test_valid_d(self):
        self.assertEqual([2, 3, 5, 6, 7], valid_d(7))

    def test_given(self):
        self.assertAlmostEqual(5, solve_first(7))


if __name__ == '__main__':
    unittest.main()
