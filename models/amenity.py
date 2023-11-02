#!/usr/bin/python3

"""
Module that defines the Amenity class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for representing amenities in the AirBnB clone.

    Attributes:
    - name (str): the name of the amenity (empty string by default).
    """

    name = ""
