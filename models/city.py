#!/usr/bin/python3

"""
Module that defines the City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for representing cities in the application.

    Attributes:
    - state_id (str): the ID of the associated state.
    - name (str): the name of the city (empty string by default).
    """

    state_id = ""
    name = ""
