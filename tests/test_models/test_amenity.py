#!/user/bin/python3
""" This module contains amenity tests """
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):

    """ Test Amenity class """

    def test_exist(self):
        """ See if instances exist """
        self.assertTrue(hasattr(Amenity, "name"))

    def test_id(self):
        """ Test id """
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_attr(self):
        """ Test naming """
        a1 = Amenity()
        a1.name = "Pizza"
        self.assertEqual(a1.name, "Pizza")

    def test_doc(self):
        """ Test doc """
        self.assertIsNotNone(Amenity.__doc__)

if __name__ == '__main__':
    unittest.main()
