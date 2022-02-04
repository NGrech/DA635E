import unittest
from parameterized import parameterized
from unittest import result

from rovar import rovar

# Testing Cases 

class TestRovar(unittest.TestCase):

    def test_null_input_encode(self):
        # Test null input case
        data = None
        rov = rovar.Rovar()
        result = rov.enrove(data)
        self.assertEqual(result, None)

    def test_null_input_decode(self):
        # Test null input case
        data = None
        rov = rovar.Rovar()
        result = rov.derove(data)
        self.assertEqual(result, None)

    def test_empty_input_encode(self):
        # Test empty input encode case
        data = ""
        rov = rovar.Rovar()
        result = rov.enrove(data)
        self.assertEqual(result, "")

    def test_empty_input_decode(self):
        # Test empty input decode case
        data = ""
        rov = rovar.Rovar()
        result = rov.derove(data)
        self.assertEqual(result, "")

    @parameterized.expand([
        ('b','bob'),('c','coc'),('d','dod'),('f','fof'),
        ('g','gog'),('h','hoh'),('j','joj'),('k','kok'),
        ('l','lol'),('m','mom'),('n','non'),('p','pop'),
        ('q','qoq'),('s','sos'),('t','tot'),('v','vov'),
        ('w','wow'),('x','xox'),('y','yoy'),('z','zoz'),
    ])
    def test_lower_case_constants_encode(self, data, expected):
        # Lower case constants test
        rov = rovar.Rovar()
        result = rov.enrove(data)
        self.assertEqual(result, expected)

# TODO: Upper case constants test 

# TODO: Lower case vowel tests 

# TODO: Upper case vowel tests 

# TODO: Number tests

# TODO: Symbols test

# TODO: White space test 

# TODO: Non empty string test 

if __name__ == '__main__':
    unittest.main()