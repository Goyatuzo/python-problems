import unittest

from before_an_exam import before_an_exam as foo

class TestBeforeAnExam(unittest.TestCase):
    def test_given(self):
        self.assertEqual(['NO', ''], foo(1, 48, [(5, 7)]))
        self.assertEqual(['YES', '1 4 '], foo(2, 5, [(0, 1), (3, 5)]))

    def test_tests(self):
        self.assertEqual(['NO', ''], foo(1, 1, [(5, 6)]))
        self.assertEqual(['YES', '5 0 '], foo(2, 5, [(4, 6), (0, 0)]))

if __name__ == '__main__':
    unittest.main()
