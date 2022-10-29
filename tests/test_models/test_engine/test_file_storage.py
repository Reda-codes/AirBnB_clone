#!/usr/bin/python3
"""Unittest to test FileStorage class"""
import unittest
import json
import os
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """testing file storage"""

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        tmp = storage.all()
        self.assertIsInstance(tmp, dict)

    def test_new(self):
        """ New object is added"""
        new = BaseModel()
        for obj in storage.all().values():
            tmp = obj
        self.assertTrue(tmp is obj)

    def test_save(self):
        """save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects"""
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            updated = obj
        self.assertEqual(new.to_dict()['id'], updated.to_dict()['id'])
