import unittest

from secure_container import meets_criteria_two


class TestSecureContainer(unittest.TestCase):

    def test_part_two_given(self):
        self.assertEqual(True, meets_criteria_two(777777))
        self.assertEqual(True, meets_criteria_two(778899))
        self.assertEqual(True, meets_criteria_two(778889))
        self.assertEqual(False, meets_criteria_two(768889))


if __name__ == '__main__':
    unittest.main()
