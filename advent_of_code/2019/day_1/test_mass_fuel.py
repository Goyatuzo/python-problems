import unittest

from mass_fuel import solve_first, solve_recursive


class TestMassFuel(unittest.TestCase):
    def test_part_one_given(self):
        self.assertEqual(2, solve_first(12))
        self.assertEqual(2, solve_first(14))
        self.assertEqual(654, solve_first(1969))
        self.assertEqual(33583, solve_first(100756))

    def test_part_two_given(self):
        self.assertEqual(2, solve_recursive(14))
        self.assertEqual(966, solve_recursive(1969))
        self.assertEqual(50346, solve_recursive(100756))


if __name__ == '__main__':
    unittest.main()
