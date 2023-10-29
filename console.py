#!/usr/bin/python3
"""command interpreter"""


import re
import cmd
import json
from datetime import datetime
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class cmd """
    prompt = "(hbnb)"
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'Amenity': Amenity, 'City': City,
        'State': State, 'Review': Review
    }

    def do_quit(self, args):
        """quit interpreter"""
        return True

    def do_EOF(self, args):
        """End of file"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    @classmethod
    def class_exists(cls, args):
        """Verifies class and checks if it is in the class list"""
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in cls.classes:
            print("** class doesn't exist **")
            return False

        return True

    @staticmethod
    def id_verification(args):
        """Verifies id of class."""
        if len(args) < 2:
            print("** instance id missing **")
            return False

        objects = models.storage.all()
        string_key = str(args[0]) + '.' + str(args[1])
        if string_key not in objects.keys():
            print("** no instance found **")
            return False

        return True
    
    def do_create(self, arg):
        """creating"""

        if not arg:
            print("** class name missing **")
            return

        arguments = re.findall(r'(?:"[^"]*"|[^"\s]+)', arg)
        
        if not arguments:
            print("** missing argument(s) **")
            return

        class_n = arguments[0]

        if class_n not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        my_dict = {}
        for i in arguments[1:]:
            m = re.match(r'([^=]+)=(.*)', i)
            if m:
                k, j = m.groups()
                j = j.replace('\\"', '"')
                my_dict[k] = j
        my_dict['created_at'] = datetime.now().isoformat()
        my_dict['updated_at'] = datetime.now().isoformat()

        my_instance = HBNBCommand.classes[class_n](**my_dict)
        storage.save()
        print(my_instance)

    def do_show(self, args):
        """show class and id"""
        new = args.partition(" ")
        class_n = new[0]
        class_id = new[2]

        if class_id and ' ' in class_id:
            class_id = class_id.partition(' ')[0]

        if not class_n:
            print("** class name missing **")
            return

        if class_n not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not class_id:
            print("** instance id missing **")
            return

        key = class_n + "." + class_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """destroy"""
        new = args.partition(" ")
        class_n = new[0]
        class_id = new[2]
        if class_id and ' ' in class_id:
            class_id = class_id.partition(' ')[0]

        if not class_n:
            print("** class name missing **")
            return

        if class_n not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not class_id:
            print("** instance id missing **")
            return

        key = class_n + "." + class_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        my_list = []
        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for i, j in storage._FileStorage__objects.items():
                my_list.append(str(j))
        else:
            for i, j in storage._FileStorage__objects.items():
                my_list.append(str(j))
        
        print(my_list)

    def do_update(self, arg):
        if not arg:
            print("** class name missing **")
            return

        args = re.findall(r'(?:"[^"]*"|[^"\s]+)', arg)
        class_name = args[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        params = {}
        for param in args[1:]:
            match = re.match(r'([^=]+)=(.*)', param)
            if match:
                key, value = match.groups()
                value = value.replace('_', ' ').replace('\\"', '"')
                params[key] = value

        if '__class__' in params:
            del params['__class__']

        if 'id' not in params:
            print("** instance id missing **")
            return

        obj_id = params['id']
        key = class_name + "." + obj_id

        if key not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[key]

        for attr_name, attr_value in params.items():
            setattr(obj, attr_name, attr_value)

        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
