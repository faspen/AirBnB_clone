#!/user/bin/python3
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):

    """ Test State class """

    def test_exist(self):
        """see if instances exits"""
        self.assertTrue(hasattr(State, "name"))

    def test_id(self):
        """Test id"""
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    def test_attr(self):
        """Test naming"""
        s1 = State()
        s1.name = "Montana"
        self.assertEqual(s1.name, "Montana")

    def test_doc(self):
        """ Test doc """
        self.assertIsNotNone(State.__doc__)

if __name__ == '__main__':
    unittest.main()
