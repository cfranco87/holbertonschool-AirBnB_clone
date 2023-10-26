#!/usr/bin/python3


class FileStorage:
    """created class FileStorage"""
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    @property
    def get_file_path(self):
        return self.__file_path

    @file_path.setter
    def set_file_path(self, file_path):
        self.__file_path = file_path

    @property
    def get_object(self)
        return self.__objects

    @object.setter
    def set_objects(self, obj):

    def all(self):
        """returns the dictionary"""
    return self.__object

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(filename, 'w') as file:
            save_data = json.dumps(self.__objects, default = lambda obj, obj.__dict__)
            file.write(save_data)

    def reload(self, save_data):
        with open(filename, 'r') as file:
            save_data = file.read()
            self.__objects = json.loads(save_data)
