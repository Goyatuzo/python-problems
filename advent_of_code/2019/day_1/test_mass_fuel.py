import unittest

from mass_fuel import solve_first


class TestMassFuel(unittest.TestCase):
    def test_given(self):
        self.assertEqual(2, solve_first(12))
        self.assertEqual(2, solve_first(14))
        self.assertEqual(654, solve_first(1969))
        self.assertEqual(33583, solve_first(100756))


if __name__ == '__main__':
    unittest.main()
