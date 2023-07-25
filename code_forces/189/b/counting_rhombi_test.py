import unittest

from counting_rhombi import counting_rhombi as foo

class Test_Counting_rhombi(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(foo(2, 2), 1)

    def test_given_2(self):
        self.assertEqual(foo(1, 2), 0)

    def test_self(self):
        self.assertEqual(foo(4, 4), 10)


if __name__ == '__main__':
    unittest.main()
