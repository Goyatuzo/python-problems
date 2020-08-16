import unittest

from omkar_and_password import omkar_and_password as foo

class TestOmkarAndPassword(unittest.TestCase):
    def test_given(self):
        self.assertEqual(1, foo([2, 1, 3, 1]))
        self.assertEqual(2, foo([420, 420]))

if __name__ == '__main__':
    unittest.main()
