#!/usr/bin/python3

"""
Module that defines the BaseModel class.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class that defines common attributes and methods.

    Attributes:
    - id (str): a unique identifier for the instance.
    - created_at (datetime): the date and time when the instance is created.
    - updated_at (datetime): the date and time when the instance is updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        If kwargs is not empty, initialize instance using provided dictionary.
        If kwargs is empty, create a new instance with unique id and dates.

        Args:
        - *args: not used.
        - **kwargs: a dictionary with attributes to initialize the instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, date)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current date and time.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        """
        new_dict = self.__dict__.copy()

        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
