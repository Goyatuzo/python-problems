import unittest

from domino_piling import domino_piling as foo

class TestDominoPiling(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(4, foo(2, 4))

    def test_given_2(self):
        self.assertEqual(4, foo(3, 3))

    def test_1(self):
        self.assertEqual(0, foo(1, 1))


if __name__ == '__main__':
    unittest.main()
