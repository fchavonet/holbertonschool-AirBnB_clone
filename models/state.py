#!/usr/bin/python3

"""
Module that defines the State class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for representing states in the AirBnB clone.

    Attributes:
    - name (str): the name of the state (empty string by default).
    """

    name = ""
