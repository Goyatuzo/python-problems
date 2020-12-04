import unittest

from toboggan import tobaggan_one, tobaggan_gen, tobaggan_two, get_file

class TestToboggan(unittest.TestCase):
    def test_given_one(self):
        self.assertEqual(7, tobaggan_one('test.txt'))

    def f(self):
        return get_file('test.txt')

    def test_given_two_one(self):
        fc = self.f()
        self.assertEqual(2, tobaggan_gen(fc, 1, 1))

    def test_given_two_two(self):
        fc = self.f()
        self.assertEqual(7, tobaggan_gen(fc, 3, 1))

    def test_given_two_three(self):
        fc = self.f()
        self.assertEqual(3, tobaggan_gen(fc, 5, 1))

    def test_given_two_four(self):
        fc = self.f()
        self.assertEqual(4, tobaggan_gen(fc, 7, 1))

    def test_given_two_five(self):
        fc = self.f()
        self.assertEqual(2, tobaggan_gen(fc, 1, 2))

    def test_given_two(self):
        self.assertEqual(336, tobaggan_two('test.txt'))

if __name__ == '__main__':
    unittest.main()
