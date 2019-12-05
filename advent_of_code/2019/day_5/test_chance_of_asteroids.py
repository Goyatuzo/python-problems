import unittest
from unittest.mock import patch

from chance_of_asteroids import process_opcodes, process_immediate_mode


class TestChanceOfAsteroids(unittest.TestCase):
    def test_immediate_mode_processing(self):
        self.assertEqual((2, True, False, True), process_immediate_mode(1002))
        self.assertEqual((0, False, False, True), process_immediate_mode(1100))

    def test_from_program_alarm(self):
        self.assertEqual([2, 0, 0, 0, 99], process_opcodes([1, 0, 0, 0, 99]))
        self.assertEqual([2, 3, 0, 6, 99], process_opcodes([2, 3, 0, 3, 99]))
        self.assertEqual([2, 4, 4, 5, 99, 9801],
                         process_opcodes([2, 4, 4, 5, 99, 0]))
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99],
                         process_opcodes([1, 1, 1, 4, 99, 5, 6, 0, 99]))

        self.assertEqual([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50], process_opcodes(
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]))

    def test_given_examples(self):
        self.assertEqual([1002, 4, 3, 4, 99],
                         process_opcodes([1002, 4, 3, 4, 33]))
        self.assertEqual([1101, 100, -1, 4, 99],
                         process_opcodes([1101, 100, -1, 4, 0]))

    def test_position_equality(self):
        with patch('builtins.input', side_effect="8"):
            self.assertEqual([3, 9, 8, 9, 10, 9, 4, 9, 99, 1, 8],
                             process_opcodes([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]))
        with patch('builtins.input', side_effect="7"):
            self.assertEqual([3, 9, 8, 9, 10, 9, 4, 9, 99, 0, 8],
                             process_opcodes([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]))

    def test_position_less_than(self):
        with patch('builtins.input', side_effect="8"):
            self.assertEqual([3, 9, 7, 9, 10, 9, 4, 9, 99, 0, 8],
                             process_opcodes([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]))
        with patch('builtins.input', side_effect="7"):
            self.assertEqual([3, 9, 7, 9, 10, 9, 4, 9, 99, 1, 8],
                             process_opcodes([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]))

    def test_immediate_equal(self):
        with patch('builtins.input', side_effect="8"):
            self.assertEqual([3, 3, 1108, 1, 8, 3, 4, 3, 99],
                             process_opcodes([3, 3, 1108, -1, 8, 3, 4, 3, 99]))
        with patch('builtins.input', side_effect="7"):
            self.assertEqual([3, 3, 1108, 0, 8, 3, 4, 3, 99],
                             process_opcodes([3, 3, 1108, -1, 8, 3, 4, 3, 99]))

    def test_immediate_less_than(self):
        with patch('builtins.input', side_effect="8"):
            self.assertEqual([3, 3, 1107, 0, 8, 3, 4, 3, 99],
                             process_opcodes([3, 3, 1107, -1, 8, 3, 4, 3, 99]))
        with patch('builtins.input', side_effect="7"):
            self.assertEqual([3, 3, 1107, 1, 8, 3, 4, 3, 99],
                             process_opcodes([3, 3, 1107, -1, 8, 3, 4, 3, 99]))

    def test_input(self):
        with patch('builtins.input', side_effect="1"):
            self.assertEqual([
                3, 13,
                1, 13, 6, 6,
                1101, 1, 238, 13,
                104, 0,
                99, 239, 23
            ], process_opcodes([
                3, 13,
                1, 13, 6, 6,
                1100, 1, 238, 13,
                104, 0,
                99, 0, 23]))

        # self.assertEqual([], process_opcodes([
        #     3, 225,               # 1
        #     1, 225, 6, 6,         # 5
        #     1100, 1, 238, 225,    # 9
        #     104, 0,               # 11
        #     1001, 210, 88, 224,   # 15
        #     101, -143, 224, 224,  # 19
        #     4, 224,               # 21
        #     22, 23]))             # 23


if __name__ == '__main__':
    unittest.main()
