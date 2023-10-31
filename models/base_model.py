#!/usr/bin/python3

"""
Module that defines the BaseModel class.
"""

import uuid
import datetime


class BaseModel:
    """
    BaseModel class that defines common attributes and methods.

    Attributes:
    - id (str): a unique identifier for the instance.
    - created_at (datetime): the date and time when the instance is created.
    - updated_at (datetime): the date and time when the instance is updated.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        Sets the unique id, creation date, and update date for the instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current date and time.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        """
        dictionary = self.__dict__.copy()

        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
