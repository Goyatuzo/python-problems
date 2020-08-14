import unittest

from registration_system import registration_system as foo

class TestRegistrationSystem(unittest.TestCase):
    def test_given(self):
        self.assertEqual('OK', foo('abacaba'))
        self.assertEqual('OK', foo('acaba'))
        self.assertEqual('abacaba1', foo('abacaba'))
        self.assertEqual('OK', foo('acab'))

if __name__ == '__main__':
    unittest.main()