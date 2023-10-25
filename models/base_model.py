#!/usr/bin/python3
"""BaseModel defines all common attributes/method"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """class BaseModel"""
    DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.initialize_iso_str()

        """remove class attribute id kwarg if it exist"""
        kwargs.pop('__class__', None)

        for key, value in kwargs.items():
            if hasattr(self, key):
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, self.DATE_FORMAT)
                setattr(self, key, value)

        if 'created_at' not in kwargs:
            self.created_at = datetime.now()

        if 'updated_at' not in kwargs:
            self.updated_at = self.created_at

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

    def initialize_iso_str(self):
        now = datetime.now()
        self.iso_str = now.isoformat()

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
