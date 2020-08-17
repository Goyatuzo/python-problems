import unittest

from omkar_and_bed_wars import omkar_and_bed_wars as foo


class TestOmkarAndWaterslide(unittest.TestCase):
    def test_given(self):
        self.assertEqual(0, foo('RLRL'))

    def test_given_two(self):
        self.assertEqual(1, foo('LRRRRL'))

    def test_given_three(self):
        self.assertEqual(1, foo('RLLRRRLL'))

    def test_given_four(self):
        self.assertEqual(3, foo('LLLLRRLRRRLL'))

    def test_given_five(self):
        self.assertEqual(2, foo('RRRRR'))

    def test_test(self):
        self.assertEqual(6, foo('RRRRRRLRRRRRRRRLLLLLL'))

    def test_test_two(self):
        self.assertEqual(
            13, foo('RRRRRLLLLLLRRRRLLLLLLRRRLLRRRRRRRRRRLLRRLLLLLLLRRRRL'))

    def test_self(self):
        self.assertEqual(0, foo('LRLL'))
        self.assertEqual(0, foo('LRRL'))

    def test_self_two(self):
        """Test only left edge not mattering."""
        self.assertEqual(0, foo('LRL'))

    def test_self_three(self):
        """Test beginning and end do not contribute to overall result."""
        self.assertEqual(0, foo('LRLR'))
        self.assertEqual(1, foo('RLRR'))

    def test_self_four(self):
        self.assertEqual(1, foo('LLL'))
        self.assertEqual(1, foo('RRR'))

    def test_self_five(self):
        """Test base case of threes"""
        self.assertEqual(0, foo('RLL'))
        self.assertEqual(0, foo('RRL'))


if __name__ == '__main__':
    unittest.main()
