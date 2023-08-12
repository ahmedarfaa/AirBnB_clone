#!/usr/bin/python3
"""intializing a state module"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    the state class only includes :
    1- name
    """
    name = ""
