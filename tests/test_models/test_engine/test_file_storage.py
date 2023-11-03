#!/usr/bin/python3

"""
Module with unittests for FileStorage class.
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Test class for FileStorage class.
    """

    def setUp(self):
        """
        Initialize FileStorage and reload data before each test.
        """
        self.storage = FileStorage()
        self.storage.reload()

    def test__file_path(self):
        """
        Test the __file_path attribute.
        """
        self.assertEqual(str, type(self.storage._FileStorage__file_path))

    def test__objects(self):
        """
        Test the __objects attribute.
        """
        self.assertEqual(dict, type(self.storage._FileStorage__objects))

    def test_all(self):
        """
        Test the all method.
        """
        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """
        Test the new method.
        """
        base = BaseModel()
        self.storage.new(base)
        self.assertIn("BaseModel." + base.id, self.storage.all().keys())
        self.assertIn(base, self.storage.all().values())

    def test_save(self):
        """
        Test the save method.
        """
        with self.assertRaises(TypeError):
            self.storage.save(None)

    def test_reload(self):
        """
        Test the reload method.
        """
        with self.assertRaises(TypeError):
            self.storage.reload(None)

    def test_1_new_object(self):
        """
        Test adding a new object to the storage.
        """
        obj = BaseModel()
        self.storage.new(obj)
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{obj.id}", all_objects)

    def test_2_save_and_reload(self):
        """
        Test saving and reloading objects to and from a JSON file.
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

    def test_4_clear_and_reload(self):
        """
        Test clearing storage and reloading it.
        """
        base = BaseModel()
        self.storage.new(base)
        self.storage.save()
        base_key = "BaseModel.{}".format(base.id)
        self.assertIn(base_key, self.storage.all())
        self.storage.all().clear()
        self.assertNotIn(base_key, self.storage.all())
        self.storage.reload()
        self.assertIn(base_key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
