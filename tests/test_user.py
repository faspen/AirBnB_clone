#!/user/bin/python3
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):

    """ Test User class """

    def test_existence(self):
        """ See if instances exist """
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
        u1 = User()
        self.assertTrue(isinstance(u1, User))

    def test_id(self):
        """ Test id """
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_attr(self):
        """ Test naming """
        u1 = User()
        u1.email = "email@example.com"
        self.assertEqual(u1.email, "email@example.com")

    def test_doc(self):
        """ Test doc """
        self.assertIsNotNone(User.__doc__)
