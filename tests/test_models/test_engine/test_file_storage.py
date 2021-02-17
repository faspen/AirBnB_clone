#!/usr/bin/python3
""" Test for file storage """
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    """ Test file storage """

    def test_attr(self):
        """ File storage test """
        house = FileStorage()
        self.assertEqual(house.all(), house.all())

if __name__ == '__main__':
    unittest.main()
