#!/usr/bin/python3
""" This module contains base model tests """
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    """ Test BaseModel Class """

    def test_existence(self):
        """ See if instances exist """
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))

    def test_doc(self):
        """ Test doc """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_id(self):
        """ Test id """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_name(self):
        """ Test naming """
        b1 = BaseModel()
        b1.name = "Base"
        self.assertEqual(b1.name, "Base")

    def test_type(self):
        """ Test type """
        b1 = BaseModel()
        self.assertTrue(isinstance(b1.created_at, datetime))
        self.assertTrue(isinstance(b1.updated_at, datetime))
        self.assertTrue(isinstance(b1.to_dict(), dict))
        self.assertTrue(hasattr(b1, 'id'))

    def test_attr(self):
        """ Test if attrs exist """
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, 'created_at'))
        self.assertTrue(hasattr(b1, 'updated_at'))
        self.assertTrue(hasattr(b1, '__init__'))
        dic = b1.to_dict()
        self.assertTrue(hasattr(dic, '__class__'))

    def test_save(self):
        """ Test save """
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, 'created_at'))
        b1.save()
        self.assertTrue(hasattr(b1, 'updated_at'))
        self.assertNotEqual(b1.created_at, b1.updated_at)

if __name__ == '__main__':
    unittest.main()
