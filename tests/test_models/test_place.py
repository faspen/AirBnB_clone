#!/user/bin/python3
""" This module contains tests for place """
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):

    """ Test Place class """

    def test_exist(self):
        """ See if instances exist """
        self.assertTrue(hasattr(Place, "name"))

    def test_attributes(self):
        """ Test default values """
        p1 = Place()
        self.assertEqual(p1.city_id, "")
        self.assertEqual(p1.user_id, "")
        self.assertEqual(p1.name, "")
        self.assertEqual(p1.description, "")
        self.assertEqual(p1.number_rooms, 0)
        self.assertEqual(p1.number_bathrooms, 0)
        self.assertEqual(p1.max_guest, 0)
        self.assertEqual(p1.price_by_night, 0)
        self.assertEqual(p1.latitude, 0.0)
        self.assertEqual(p1.longitude, 0.0)
        self.assertEqual(p1.amenity_ids, [])

    def test_id(self):
        """ Test id """
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_attr(self):
        """ Test naming """
        p1 = Place()
        p1.name = "Hotel"
        self.assertEqual(p1.name, "Hotel")

    def test_doc(self):
        """ Test doc """
        self.assertIsNotNone(Place.__doc__)

if __name__ == '__main__':
    unittest.main()
