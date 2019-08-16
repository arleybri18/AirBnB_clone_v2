#!/usr/bin/python3
"""test for DB storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                    "Cases only for DBStorage")
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = DBStorage()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                    "Cases only for DBStorage")
    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user
    """
    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass
    """
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                    "Cases only for DBStorage")
    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                    "Cases only for DBStorage")
    def test_all(self):
        """tests if all works in DB Storage"""
        storage = DBStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._DBStorage__objects)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                    "Cases only for DBStorage")
    def test_new(self):
        """test when new is created"""
        storage = DBStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])



if __name__ == "__main__":
    unittest.main()
