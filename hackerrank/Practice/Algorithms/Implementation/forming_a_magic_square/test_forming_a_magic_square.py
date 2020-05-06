import unittest

from forming_a_magic_square import formingMagicSquare

class TestBetweenTwoPoints(unittest.TestCase):
    def test_given(self):
        self.assertEqual(4, formingMagicSquare([[4, 8, 2], [4, 5,
            7], [6, 1, 6]]))

if __name__ == '__main__':
    unittest.main()
