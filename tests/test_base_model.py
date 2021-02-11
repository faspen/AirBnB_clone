#!/usr/bin/python3
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

    def test_base(self):
        """ Test base """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        b1.name = "Base"
        self.assertEqual(b1.name, "Base")
        self.assertTrue(isinstance(b1.created_at, datetime))
        self.assertTrue(isinstance(b1.updated_at, datetime))
        self.assertTrue(isinstance(b1.to_dict(), dict))
        self.assertTrue(hasattr(b1, 'id'))
        self.assertTrue(hasattr(b1, 'created_at'))
        self.assertTrue(hasattr(b1, 'updated_at'))
        dic = b1.to_dict()
        self.assertTrue(hasattr(dic, '__class__'))
