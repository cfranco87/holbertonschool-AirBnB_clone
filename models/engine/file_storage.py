#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    __classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
    }

    def all(self):
        """Returns a dictionary representation of models"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        save_it = {}
        for k, v in FileStorage.__objects.items():
            save_it[k] = v.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(save_it, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel

        try:
            with open(FileStorage.__file_path, mode="r") as my_file:
                objects = json.load(my_file)
                for key, value in objects.items():
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
