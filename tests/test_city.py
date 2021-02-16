#!/user/bin/python3
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):

    """ Test city class """

    def test_exist(self):
        """ See if instances exist """
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))

    def test_id(self):
        """ Test id """
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_attr(self):
        """ Test naming """
        c1 = City()
        c1.name = "NYC"
        self.assertEqual(c1.name, "NYC")

    def test_doc(self):
        """ Test doc """
        self.assertIsNotNone(City.__doc__)
