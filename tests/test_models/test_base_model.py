#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(clss):
        clss.new = BaseModel()
        clss.new.name = "RedRed"
        clss.new.my_num = 2020

    @classmethod
    def tearDownClass(clss):
        del clss.new
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_check_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attr(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        self.assertTrue(isinstance(self.new, BaseModel))

    def test_save(self):
        self.new.save()
        self.assertNotEqual(self.new.created_at, self.new.updated_at)

    def test_to_dict(self):
        new_dict = self.new.to_dict()
        self.assertEqual(self.new.__class__.__name__, 'BaseModel')
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
