#!/usr/bin/python3
"""This is the User class"""
from models.base_model import BaseModel


class State(BaseModel):
    """creating state class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of state."""
        super().__init__(*args, **kwargs)
