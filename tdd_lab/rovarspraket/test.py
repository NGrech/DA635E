#from typing_extensions import Self
from sre_parse import WHITESPACE
import unittest
from parameterized import parameterized
from unittest import result
import copy
import string

from rovar import rovar

# Testing Cases 

class TestRovar(unittest.TestCase):

    CONSTANTS = [
        ('b','bob'),('c','coc'),('d','dod'),('f','fof'),
        ('g','gog'),('h','hoh'),('j','joj'),('k','kok'),
        ('l','lol'),('m','mom'),('n','non'),('p','pop'),
        ('q','qoq'),('s','sos'),('t','tot'),('v','vov'),
        ('w','wow'),('x','xox'),('y','yoy'),('z','zoz'),
    ]
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'ö', 'å', 'ä']
    VOWELS_CAP = ['A', 'E', 'I', 'O', 'U', 'Ö', 'Å', 'Ä']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SYMBOLS = list(string.punctuation)
    WHITESPACE = list(string.whitespace)

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

    @parameterized.expand(CONSTANTS)
    def test_lower_case_constants_encode(self, data, expected):
        # Lower case constants encode test
        rov = rovar.Rovar()
        result = rov.enrove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(CONSTANTS)
    def test_lower_case_constants_decode(self, expected, data):
        # Lower case constants decode test
        rov = rovar.Rovar()
        result = rov.derove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(VOWELS)
    def test_lower_case_vowels_encode(self,data):
        # lower case vowel encode test
        expected = copy.copy(data)
        rov = rovar.Rovar()
        result = rov.enrove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(VOWELS)
    def test_lower_case_vowels_decode(self,data):
        # lower case vowel decode test
        expected = copy.copy(data)
        rov = rovar.Rovar()
        result = rov.derove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(VOWELS_CAP)
    def test_upper_case_vowels_encode(self,data):
        # upper case vowel encode test
        expected = copy.copy(data)
        rov = rovar.Rovar()
        result = rov.enrove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(VOWELS_CAP)
    def test_upper_case_vowels_decode(self,data):
        # upper case vowel decode test
        expected = copy.copy(data)
        rov = rovar.Rovar()
        result = rov.derove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(NUMBERS)
    def test_numbers_encode(self,data):
        # numbers encode test
        expected = copy.copy(data)
        rov = rovar.Rovar()
        result = rov.enrove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(NUMBERS)
    def test_numbers_decode(self,data):
        # numbers decode test
        expected = copy.copy(data)
        rov = rovar.Rovar()
        result = rov.derove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(SYMBOLS)
    def test_symbols_encode(self,data):
        # symbols encode test
        expected = copy.copy(data)
        rov = rovar.Rovar()
        result = rov.enrove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(SYMBOLS)
    def test_symbols_decode(self,data):
        # symbols decode test
        expected = copy.copy(data)
        rov = rovar.Rovar()
        result = rov.derove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(WHITESPACE)
    def test_whitespace_encode(self,data):
        # whitespace encode test
        expected = copy.copy(data)
        rov = rovar.Rovar()
        result = rov.enrove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(WHITESPACE)
    def test_whitespace_decode(self,data):
        # whitespace decode test
        expected = copy.copy(data)
        rov = rovar.Rovar()
        result = rov.derove(data)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
