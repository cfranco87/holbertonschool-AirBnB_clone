#!/usr/bin/python3
"""This is the Amenity class that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """creating Amenity class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of Amenity."""
        super().__init__(*args, **kwargs)
