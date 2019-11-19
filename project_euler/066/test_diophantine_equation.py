import unittest

from diophantine_equation import solve_first


class TestDiophantineEquation(unittest.TestCase):
    def test_given(self):
        self.assertAlmostEqual(5, solve_first(7))


if __name__ == '__main__':
    unittest.main()
