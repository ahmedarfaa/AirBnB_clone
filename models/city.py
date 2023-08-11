#!/usr/bin/python3
"""initiating The city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A city in the application:
    1- name
    2- state_id
    """
    name = ""
    state_id = ""
