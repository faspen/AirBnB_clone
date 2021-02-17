#!/user/bin/python3
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):

    """ Test Place class """

    def test_exist(self):
        """ See if instances exist """
        self.assertTrue(hasattr(Place, "name"))

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
