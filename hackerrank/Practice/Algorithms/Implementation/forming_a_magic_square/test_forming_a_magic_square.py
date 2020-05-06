import unittest

from forming_a_magic_square import formingMagicSquare, magic_square_delta

class TestBetweenTwoPoints(unittest.TestCase):
    def test_given(self):
        self.assertEqual(4, magic_square_delta([[4, 8, 2], [4, 5,
            7], [6, 1, 6]]))

    def test_problem(self):
        self.assertEqual([[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]]))

if __name__ == '__main__':
    unittest.main()
