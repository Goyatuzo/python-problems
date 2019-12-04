import unittest

from secure_container import solve_first, solve_second, meets_criteria_two


class TestSecureContainer(unittest.TestCase):

    def test_part_two_subset_of_one(self):
        lo = 278384
        hi = 824795

        first = solve_first(lo, hi)
        second = solve_second(lo, hi)

        self.assertTrue(set(second).issubset(set(first)))

    def test_part_two_given(self):
        self.assertTrue(meets_criteria_two(278899))
        self.assertTrue(meets_criteria_two(777777))
        self.assertTrue(meets_criteria_two(778899))
        self.assertTrue(meets_criteria_two(778889))
        self.assertFalse(meets_criteria_two(768889))
        self.assertFalse(meets_criteria_two(279999))


if __name__ == '__main__':
    unittest.main()
