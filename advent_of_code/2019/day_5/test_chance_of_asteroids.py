import unittest

from chance_of_asteroids import process_opcodes


class TestChanceOfAsteroids(unittest.TestCase):
    def test_from_program_alarm(self):
        self.assertEqual([2, 0, 0, 0, 99], process_opcodes([1, 0, 0, 0, 99]))
        self.assertEqual([2, 3, 0, 6, 99], process_opcodes([2, 3, 0, 3, 99]))
        self.assertEqual([2, 4, 4, 5, 99, 9801],
                         process_opcodes([2, 4, 4, 5, 99, 0]))
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99],
                         process_opcodes([1, 1, 1, 4, 99, 5, 6, 0, 99]))

        self.assertEqual([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50], process_opcodes(
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]))


if __name__ == '__main__':
    unittest.main()
