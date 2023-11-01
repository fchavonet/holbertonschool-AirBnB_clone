#!/usr/bin/python3

"""
Module that defines the FileStorage class.
"""

import json
import os.path


class FileStorage:
    """
    FileStorage class responsible for serializing
    and deserializing JSON files to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
        - obj: an instance of a class to be stored.
        """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes stored objects to a JSON file.
        """
        json_dict = {}

        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(json_dict, file)

    def reload(self):
        """
        Deserializes the JSON file and restores objects to the storage.
        """
        from models import base_model

        module_mapping = {
            "BaseModel": base_model,
        }

        with open(self.__file_path, "r", encoding="utf-8") as file:

            data = json.load(file)

            for key, value in data.items():
                class_name = value["__class__"]

                if class_name in module_mapping:
                    model_module = module_mapping[class_name]
                    model_class = getattr(model_module, class_name)

                obj_instance = model_class(**value)
                self.__objects[key] = obj_instance
