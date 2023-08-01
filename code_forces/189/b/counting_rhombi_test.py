import unittest

from counting_rhombi import counting_rhombi as foo

class Test_Counting_rhombi(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(foo(2, 2), 1)

    def test_given_2(self):
        self.assertEqual(foo(1, 2), 0)

    def test_actual_4(self):
        self.assertEqual(foo(4000, 1), 0)

    def test_actual_6(self):
        self.assertEqual(foo(15, 10), 1400)

if __name__ == '__main__':
    unittest.main()
