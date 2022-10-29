#!/usr/bin/python3
"""
Places test module
"""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    @classmethod
    def setUpClass(clss):
        clss.newPlace = Place()
        clss.newPlace.city_id = "Paris"
        clss.newPlace.user_id = "tj554"
        clss.newPlace.name = "apprt"
        clss.newPlace.description = "tiny appartment"
        clss.newPlace.number_rooms = 1
        clss.newPlace.number_bathrooms = 1
        clss.newPlace.max_guest = 2
        clss.newPlace.price_by_night = 25
        clss.newPlace.latitude = 0.0
        clss.newPlace.longitude = 0.0
        clss.newPlace.amenity_ids = []

    @classmethod
    def tearDownClass(clss):
        del clss.newPlace
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        self.assertTrue(issubclass(self.newPlace.__class__, BaseModel), True)

    def test_creation(self):
        self.assertIsNotNone(Place.__doc__)

    def test_attr(self):
        self.assertTrue('id' in self.newPlace.__dict__)
        self.assertTrue('created_at' in self.newPlace.__dict__)
        self.assertTrue('updated_at' in self.newPlace.__dict__)
        self.assertTrue('city_id' in self.newPlace.__dict__)
        self.assertTrue('user_id' in self.newPlace.__dict__)
        self.assertTrue('name' in self.newPlace.__dict__)
        self.assertTrue('description' in self.newPlace.__dict__)
        self.assertTrue('number_rooms' in self.newPlace.__dict__)
        self.assertTrue('number_bathrooms' in self.newPlace.__dict__)
        self.assertTrue('max_guest' in self.newPlace.__dict__)
        self.assertTrue('price_by_night' in self.newPlace.__dict__)
        self.assertTrue('latitude' in self.newPlace.__dict__)
        self.assertTrue('longitude' in self.newPlace.__dict__)
        self.assertTrue('amenity_ids' in self.newPlace.__dict__)

    def test_str(self):
        self.assertEqual(type(self.newPlace.city_id), str)
        self.assertEqual(type(self.newPlace.user_id), str)
        self.assertEqual(type(self.newPlace.name), str)
        self.assertEqual(type(self.newPlace.description), str)
        self.assertEqual(type(self.newPlace.number_rooms), int)
        self.assertEqual(type(self.newPlace.number_bathrooms), int)
        self.assertEqual(type(self.newPlace.max_guest), int)
        self.assertEqual(type(self.newPlace.price_by_night), int)
        self.assertEqual(type(self.newPlace.latitude), float)
        self.assertEqual(type(self.newPlace.longitude), float)
        self.assertEqual(type(self.newPlace.amenity_ids), list)

    def test_save(self):
        self.newPlace.save()
        self.assertNotEqual(self.newPlace.created_at, self.newPlace.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.newPlace), True)


if __name__ == "__main__":
    unittest.main()
