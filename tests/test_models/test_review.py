#!/usr/bin/python3
"""
Review test module
"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    @classmethod
    def setUpClass(clss):
        clss.new = Review()
        clss.new.place_id = "tj445"
        clss.new.user_id = "reda"
        clss.new.text = "good"

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
        self.assertIsNotNone(Review.__doc__)

    def test_attr(self):
        self.assertTrue('id' in self.new.__dict__)
        self.assertTrue('created_at' in self.new.__dict__)
        self.assertTrue('updated_at' in self.new.__dict__)
        self.assertTrue('place_id' in self.new.__dict__)
        self.assertTrue('text' in self.new.__dict__)
        self.assertTrue('user_id' in self.new.__dict__)

    def test_sttr(self):
        self.assertEqual(type(self.new.text), str)
        self.assertEqual(type(self.new.user_id), str)
        self.assertEqual(type(self.new.place_id), str)

    def test_save(self):
        self.new.save()
        self.assertNotEqual(self.new.created_at, self.new.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.new), True)


if __name__ == "__main__":
    unittest.main()
