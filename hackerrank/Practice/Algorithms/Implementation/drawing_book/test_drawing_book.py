import unittest

from drawing_book import pageCount

class TestDrawingBook(unittest.TestCase):
    def test_given(self):
        self.assertEqual(1, pageCount(6, 2))
        self.assertEqual(0, pageCount(5, 4))

if __name__ == '__main__':
    unittest.main()
