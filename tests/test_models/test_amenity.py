#!/usr/bin/python3
"""Amenity module Unittest"""

import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(clss):
        clss.new = Amenity()
        clss.new.name = "pool"

    @classmethod
    def tearDownClass(clss):
        del clss.new
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_creation(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_attr(self):
        self.assertTrue('name' in self.new.__dict__)
        self.assertTrue('id' in self.new.__dict__)
        self.assertTrue('created_at' in self.new.__dict__)
        self.assertTrue('updated_at' in self.new.__dict__)

    def test_str(self):
        self.assertEqual(type(self.new.name), str)

    def test_subclss(self):
        self.assertTrue(issubclass(self.new.__class__, BaseModel), True)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.new), True)


if __name__ == "__main__":
    unittest.main()
