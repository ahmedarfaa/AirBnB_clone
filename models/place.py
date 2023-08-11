#!/usr/bin/python3
"""intializing place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    the place class inclues some information required such as :
    1-name
    2-user_id
    3-city_id
    4-description
    5-number_bathrooms
    6-price_by_night
    7-number_rooms
    8-longitude
    9-latitude
    10-max_guest
    11-amenity_ids
    """

    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    price_by_night = 0
    number_rooms = 0
    longitude = 0.0
    latitude = 0.0
    max_guest = 0
    amenity_ids = []
