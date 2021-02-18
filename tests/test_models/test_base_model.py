#!/usr/bin/python3
""" This module contains base model tests """
from models.base_model import BaseModel
import unittest
from datetime import datetime
import pep8


class TestBaseModel(unittest.TestCase):

    """ Test BaseModel Class """

    def test_pep8(self):
        """ Test pep8 format """
        style = pep8.StyleGuide(quiet=True)
        f1 = 'models/base_model.py'
        f2 = 'tests/test_models/test_base_model.py'

        check = style.check_files((f1, f2))
        err = "Code format errors found"
        self.assertEqual(check.total_errors, 0, err)

    def test_existence(self):
        """ See if instances exist """
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_doc(self):
        """ Test doc """
        self.assertIsNotNone(BaseModel.__doc__)
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)

    def test_id(self):
        """ Test id """
        b1 = BaseModel()
        self.assertEqual(b1.id, b1.id)
        self.assertEqual(b1.created_at, b1.created_at)
        self.assertEqual(b1.updated_at, b1.updated_at)
        self.assertEqual(str(b1), str(b1))
        self.assertDictEqual(b1.to_dict(), b1.to_dict())
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

    def test_kwargs(self):
        """ Test kwargs """
        dic = {"created_at": "2021-02-17T17:13:24.152743",
               "id": "4d8fdd8d-e69d-448e-acd7-3e681d7d8e19",
               "updated_at": "2021-02-17T17:13:24.152752"}

        b1 = BaseModel(**dic)

        self.assertEqual(b1.id, "4d8fdd8d-e69d-448e-acd7-3e681d7d8e19")
        self.assertEqual(
            b1.created_at,
            datetime(2021,
                     2,
                     17,
                     17,
                     13,
                     24,
                     152743))
        self.assertEqual(
            b1.updated_at,
            datetime(2021,
                     2,
                     17,
                     17,
                     13,
                     24,
                     152752))
        self.assertEqual(str(b1), str(b1))
        b1.save()
        self.assertEqual(b1.updated_at, b1.updated_at)
        self.assertEqual(b1.__class__, type(b1))

if __name__ == '__main__':
    unittest.main()
