import unittest

from omkar_and_waterslide import omkar_and_waterslide as foo

class TestOmkarAndWaterslide(unittest.TestCase):
    def test_given(self):
        self.assertEqual(3, foo([5, 3, 2, 5]))
        self.assertEqual(2, foo([1, 2, 3, 5, 3]))
        self.assertEqual(0, foo([1, 1, 1]))

if __name__ == '__main__':
    unittest.main()
