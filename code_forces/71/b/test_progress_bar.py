import unittest

from progress_bar import progress_bar as foo

class TestWayTooLongWords(unittest.TestCase):
    def test_given(self):
        self.assertEqual([10, 10, 10, 10, 10, 4, 0, 0, 0, 0], foo([10, 10, 54]))
        self.assertEqual([13, 13, 13, 13, 0, 0, 0, 0, 0, 0, 0], foo([11, 13, 37]))

if __name__ == '__main__':
    unittest.main()