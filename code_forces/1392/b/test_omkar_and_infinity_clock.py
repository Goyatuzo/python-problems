import unittest

from omkar_and_infinity_clock import omkar_and_infinity_clock as foo

class TestOmkarAndInfinityClock(unittest.TestCase):
    def test_given(self):
        self.assertEqual('391 0', foo(1, [-199, 192]))
        self.assertEqual('0 6 1 3 5', foo(19, [5, -1, 4, 2, 0]))
        self.assertEqual('0', foo(2, [69]))
    
    def test_self(self):
        self.assertEqual('0', foo(1, [50]))

if __name__ == '__main__':
    unittest.main()
