#!/usr/bin/python3

"""
Module with unittests for FileStorage class.
"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Test class for FileStorage class.
    """

    def test_1_new_object(self):
        """
        Test adding a new object to the storage.
        """
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        all_objects = storage.all()
        self.assertIn(f"BaseModel.{obj.id}", all_objects)

    def test_2_save_and_reload(self):
        """
        Test saving and reloading objects to and from JSON file.
        """
        storage1 = FileStorage()
        obj1 = BaseModel()
        storage1.new(obj1)
        storage1.save()

        storage2 = FileStorage()
        storage2.reload()
        all_objects = storage2.all()
        self.assertIn(f"BaseModel.{obj1.id}", all_objects)

    def test_3_reload_existing_file(self):
        """
        Test reloading objects from an existing JSON file.
        """
        storage1 = FileStorage()
        obj1 = BaseModel()
        storage1.new(obj1)
        storage1.save()

        storage2 = FileStorage()
        storage2.reload()
        all_objects = storage2.all()
        self.assertIn(f"BaseModel.{obj1.id}", all_objects)


if __name__ == "__main__":
    unittest.main()
