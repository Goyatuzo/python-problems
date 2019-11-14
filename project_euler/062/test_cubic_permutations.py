import unittest

from cubic_permutations import solve_first


class TestCubicPermutations(unittest.TestCase):
    def test_given(self):
        self.assertAlmostEqual(41063625, solve_first(3))


if __name__ == '__main__':
    unittest.main()
