import unittest

from omkar_and_bed_wars import omkar_and_bed_wars as foo


class TestOmkarAndWaterslide(unittest.TestCase):
    def test_given(self):
        self.assertEqual(0, foo('RLRL'))
        self.assertEqual(1, foo('LRRRRL'))
        self.assertEqual(1, foo('RLLRRRLL'))
        self.assertEqual(3, foo('LLLLRRLRRRLL'))
        self.assertEqual(2, foo('RRRRR'))


if __name__ == '__main__':
    unittest.main()
