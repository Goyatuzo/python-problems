import unittest

from cubic_permutations import solve_first, permute_numbers


class TestCubicPermutations(unittest.TestCase):
    def test_permute_numbers(self):
        self.assertEqual(2, len(permute_numbers(12)))
        self.assertEqual(6, len(permute_numbers(123)))

    def test_given(self):
        self.assertAlmostEqual(41063625, solve_first(3))


if __name__ == '__main__':
    unittest.main()
