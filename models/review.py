#!/usr/bin/python3
""" defining a review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The review class is used to have :
    1- text
    2- user_id
    3- place_id
    """
    text = ""
    user_id = ""
    place_id = ""
