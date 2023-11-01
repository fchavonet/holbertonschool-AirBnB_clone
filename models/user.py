#!/usr/bin/python3

"""
Module that define User class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines the User class which inherits from BaseModel.

    Attributes:
    - email (str): an empty string representing the user's email address.
    - password (str): an empty string representing the user's password.
    - first_name (str): an empty string representing the user's first name.
    - last_name (str): an empty string representing the user's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
