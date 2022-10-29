#!/usr/bin/python3

import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(clss):
        clss.usr = User()
        clss.usr.first_name = "Reda"
        clss.usr.last_name = "BHH"
        clss.usr.email = "reda@gmail.com"
        clss.usr.password = "fffff"

    @classmethod
    def tearDownClass(clss):
        del clss.usr
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_creation(self):
        self.assertIsNotNone(User.__doc__)

    def test_attr(self):
        self.assertTrue('email' in self.usr.__dict__)
        self.assertTrue('id' in self.usr.__dict__)
        self.assertTrue('created_at' in self.usr.__dict__)
        self.assertTrue('updated_at' in self.usr.__dict__)
        self.assertTrue('password' in self.usr.__dict__)
        self.assertTrue('first_name' in self.usr.__dict__)
        self.assertTrue('last_name' in self.usr.__dict__)

    def test_str(self):
        self.assertEqual(type(self.usr.email), str)
        self.assertEqual(type(self.usr.password), str)
        self.assertEqual(type(self.usr.first_name), str)
        self.assertEqual(type(self.usr.first_name), str)

    def test_subclss(self):
        self.assertTrue(issubclass(self.usr.__class__, BaseModel), True)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.usr), True)


if __name__ == "__main__":
    unittest.main()
