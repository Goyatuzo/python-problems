import unittest

from passport import passport_one

class TestPassport(unittest.TestCase):
    def test_given_one(self):
        self.assertEqual(2, passport_one('test.txt'))

if __name__ == '__main__':
    unittest.main()
