#!/usr/bin/python3
"""This is the Review class inherit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """creates Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of City."""
        super().__init__(*args, **kwargs)
