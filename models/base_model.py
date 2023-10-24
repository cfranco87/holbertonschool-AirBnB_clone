#!/usr/bin/python3
"""BaseModel defines all common attributes/method"""
from uuid import uuid4
from datetime import datetime



class BaseModel:
    """class BaseModel"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.create_at = datetime.now()
        self.updated_at = self.create_at

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__""""
        return self.__dict__

    now = datetime.now()

    iso_str = now.isoformat()

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"[{class name}]({self.id}) {self.__dict__})
