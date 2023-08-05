import unittest

from remove_element import remove_element as foo

class Test_Remove_Element(unittest.TestCase):
    def test_given_1(self):
        t = [3, 2, 2, 3]
        self.assertEqual(foo(t, 3), 2)
        print(t)

    def test_given_2(self):
        self.assertEqual(foo([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)

    def test_self_1(self):
        self.assertEqual(foo([2, 2, 2, 3], 2), 1)


if __name__ == '__main__':
    unittest.main()
