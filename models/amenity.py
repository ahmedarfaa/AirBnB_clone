#!/usr/bin/python3
""" defining the amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    this amenity class provides the :
    name of the amenity for state\city
    """
    name = ""
