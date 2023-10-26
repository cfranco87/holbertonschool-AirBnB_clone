#!/usr/bin/python3
"""This is the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """A new class User inheriting BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of User"""
        super().__init__(*args, **kwargs)
