#!/user/bin/python3
""" This module contains tests for review """
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):

    """ Test Review class """

    def test_exist(self):
        """ See if instances exist """
        self.assertTrue(hasattr(Review, "text"))

    def test_attributes(self):
        """ Test default values """
        r1 = Review()
        self.assertEqual(r1.place_id, "")
        self.assertEqual(r1.user_id, "")
        self.assertEqual(r1.text, "")

    def test_id(self):
        """ Test id """
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_attr(self):
        """ Test naming """
        r1 = Review()
        r1.text = "Pizza"
        self.assertEqual(r1.text, "Pizza")

    def test_doc(self):
        """ Test doc """
        self.assertIsNotNone(Review.__doc__)

if __name__ == '__main__':
    unittest.main()
