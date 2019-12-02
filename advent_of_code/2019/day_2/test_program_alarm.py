import unittest

from program_alarm import solve_first


class TestProgramAlarm(unittest.TestCase):
    def test_part_one_given(self):
        self.assertEqual([2, 0, 0, 0, 99], solve_first([1, 0, 0, 0, 99]))
        self.assertEqual([2, 3, 0, 6, 99], solve_first([2, 3, 0, 3, 99]))
        self.assertEqual([2, 4, 4, 5, 99, 9801],
                         solve_first([2, 4, 4, 5, 99, 0]))
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99],
                         solve_first([1, 1, 1, 4, 99, 5, 6, 0, 99]))


if __name__ == '__main__':
    unittest.main()
