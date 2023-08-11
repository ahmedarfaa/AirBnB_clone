#!usr/bin/python3
"""initiating a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The user class is a class that creates a new user
    with some features such as
    1- email
    2- password
    3- fisrt name
    4- last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
