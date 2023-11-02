#!/usr/bin/python3

"""
Module that defines the Review class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for representing reviews in the AirBnB clone.

    Attributes:
    - place_id (str): the ID of the associated place (empty string by default).
    - user_id (str): the ID of the associated user (empty string by default).
    - text (str): the review text (empty string by default).
    """

    place_id = ""
    user_id = ""
    text = ""
