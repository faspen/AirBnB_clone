#!/usr/bin/python3
""" Test for file storage """
import unittest
from models.engine.file_storage import FileStorage
import pep8
from models.base_model import BaseModel
import json


class TestFileStorage(unittest.TestCase):

    """ Test file storage """

    def test_pep8(self):
        """ Test pep8 """
        pep = pep8.StyleGuide(quiet=True)
        check = pep.check_files(["models/base_model.py"])
        self.assertEqual(check.total_errors, 0)

    def test_doc(self):
        """ Test doc """
        self.assertIsNotNone(FileStorage.__doc__)
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)

    def test_attr(self):
        """ File storage test """
        house = FileStorage()
        self.assertEqual(house.all(), house.all())

if __name__ == '__main__':
    unittest.main()
