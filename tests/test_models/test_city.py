#!/usr/bin/python3
"""
City test module
"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    @classmethod
    def setUpClass(clss):
        clss.new = City()
        clss.new.name = "NewYork"
        clss.new.state_id = "NY"

    @classmethod
    def tearDownClass(clss):
        del clss.new
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        self.assertTrue(issubclass(self.new.__class__, BaseModel), True)

    def test_creation(self):
        self.assertIsNotNone(City.__doc__)

    def test_attr(self):
        self.assertTrue('id' in self.new.__dict__)
        self.assertTrue('created_at' in self.new.__dict__)
        self.assertTrue('updated_at' in self.new.__dict__)
        self.assertTrue('name' in self.new.__dict__)
        self.assertTrue('state_id' in self.new.__dict__)

    def test_sttr(self):
        self.assertEqual(type(self.new.name), str)
        self.assertEqual(type(self.new.state_id), str)

    def test_save(self):
        self.new.save()
        self.assertNotEqual(self.new.created_at, self.new.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.new), True)


if __name__ == "__main__":
    unittest.main()
