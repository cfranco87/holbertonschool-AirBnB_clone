#!/usr/bin/python3
"""This is the City class inherit from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """creating City class"""
    
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of City."""
        super().__init__(*args, **kwargs)
