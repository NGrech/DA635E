from asyncio.windows_events import NULL
import unittest
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


# TODO: Lower case constants test

# TODO: Upper case constants test 

# TODO: Lower case vowel tests 

# TODO: Upper case vowel tests 

# TODO: Number tests

# TODO: Symbols test

if __name__ == '__main__':
    unittest.main()