import unittest

from pw_phil import pw_phil_valid

class TestPasswordPhilosophy(unittest.TestCase):
    def test_given_one(self):
        self.assertEqual(True, pw_phil_valid('1-3 a: abcde'))
    def test_given_two(self):
        self.assertEqual(False, pw_phil_valid('1-3 b: cdefg'))
    def test_given_three(self):
        self.assertEqual(True, pw_phil_valid('2-9 c: ccccccccc'))


if __name__ == '__main__':
    unittest.main()
