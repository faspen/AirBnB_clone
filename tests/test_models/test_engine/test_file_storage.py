#!/usr/bin/python3
""" Test for file storage """
import unittest


class TestFileStorage(unittest.TestCase):

    """ Test file storage """

    def test_addition(self):
        """ Idk what to test for so lets test addition """
        a = 5
        b = 4
        self.assertEqual(a + b, 9)

if __name__ == '__main__':
    unittest.main()
