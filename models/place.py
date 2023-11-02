#!/usr/bin/python3

"""
Module that defines the Place class.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class for representing places in the the AirBnB clone.

    Attributes:
    - city_id (str): the ID of the associated city (empty string by default).
    - user_id (str): the ID of the associated user (empty string by default).
    - name (str): the name of the place (empty string by default).
    - description (str): the place description (empty string by default).
    - number_rooms (int): the number of rooms (0 by default).
    - number_bathrooms (int): the number of bathrooms (0 by default).
    - max_guest (int): the maximumu number of guests (0 by default).
    - price_by_night (int): the price per night for the place (0 by default).
    - latitude (float): the latitude of the place (0.0 by default).
    - longitude (float): the longitude of the place (0.0 by default).
    - amenity_ids (list): a list of IDs of associated amenities.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
