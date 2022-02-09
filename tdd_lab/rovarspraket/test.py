#from typing_extensions import Self
import unittest
from parameterized import parameterized
import copy
import string

from rovar import rovar

# Testing Cases 

class TestRovar(unittest.TestCase):

    CONSONANT = [
        ('b','bob'),('c','coc'),('d','dod'),('f','fof'),
        ('g','gog'),('h','hoh'),('j','joj'),('k','kok'),
        ('l','lol'),('m','mom'),('n','non'),('p','pop'),
        ('q','qoq'),('s','sos'),('t','tot'),('v','vov'),
        ('w','wow'),('x','xox'),('z','zoz'),
    ]
    
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'ö', 'å', 'ä', 'y']
    VOWELS_CAP = ['A', 'E', 'I', 'O', 'U', 'Ö', 'Å', 'Ä', 'Y']
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

    @parameterized.expand(CONSONANT)
    def test_lower_case_consonants_encode(self, data, expected):
        # Lower case consonants encode test
        rov = rovar.Rovar()
        result = rov.enrove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(CONSONANT)
    def test_lower_case_consonants_decode(self, expected, data):
        # Lower case consonants decode test
        rov = rovar.Rovar()
        result = rov.derove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(CONSONANT)
    def test_upper_case_consonants_encode(self, data, expected):
        # Upper case consonants encode test
        data = data.upper()
        expected = expected[0].upper() + expected[1] + expected[2].upper()
        rov = rovar.Rovar()
        result = rov.enrove(data)
        self.assertEqual(result, expected)

    @parameterized.expand(CONSONANT)
    def test_upper_case_consonants_decode(self, expected, data):
        # Upper case consonants decode test
        data = data[0].upper() + data[1] + data[2].upper()
        expected = expected.upper()
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
        
    def test_pangram_encode(self):
        # test encoding of a pangram
        data = 'FAQ om Schweiz: Klöv du trång pjäxby?'
        expected = 'FoFAQoQ omom SoScochohwoweizoz: KoKlolövov dodu totrorånongog popjojäxoxboby?'

        rov = rovar.Rovar()
        result = rov.enrove(data)
        self.assertEqual(result, expected)

    def test_pangram_decode(self):
        # test encoding of a pangram
        data = 'FoFAQoQ omom SoScochohwoweizoz: KoKlolövov dodu totrorånongog popjojäxoxboby?'
        expected = 'FAQ om Schweiz: Klöv du trång pjäxby?'

        rov = rovar.Rovar()
        result = rov.derove(data)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
