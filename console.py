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

        arguments = re.findall(r'(?:"[^"]*"|[^"\s]+)', arg)

        if arguments[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        my_dict = {}
        for i in arguments[1:]:
            m = re.match(r'([^=]+)=(.*)', i)
            if m:
                k, j = m.group
                j = j.replace('\\"', '"')
                my_dict[i] = j
        my_dict['created_at'] = datetime.now().isoformat()
        my_dict['updated_at'] = datetime.now().isoformat()

        my_instance = HBNBCommand.classes[arguments[0]](**my_dict)
        storage.save()
        print(my_instance)

    def do_show(self, args):
        """show class and id"""
        arguments = args.split()

        if len(arguments) < 1:
            print("** class name missing **")
            return

        class_name = arguments[0]
        try:
            obj_id = arguments[1]
        except IndexError:
            print("** instance id missing **")
            return

        if not self.class_exists(class_name):
            print("** class doesn't exist **")
            return

        string_key = class_name + '.' + obj_id
        objects = models.storage.all()

        if string_key in objects:
            print(objects[string_key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """destroy"""
        arguments = args.split()
        if not self.class_exists(args):
            return
        if not self.id_verification(args):
            return
        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        models.storage.delete(objects[string_key])
        models.storage.save()

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

    def do_update(self, line):
        if not args:
            print("** class name missing **")

        arguments = re.findall(r'(?:"[^"]*"|[^"\s]+)', arg)

        if arguments[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        my_dict = {}
        for i in arguments[1:]:
            m = re.match(r'([^=]+)=(.*)', i)
            if m:
                k, j = m.group
                j = j.replace('\\"', '"')
                my_dict[i] = j

        if 'id' not in my_dict:
            print('** instance id missing **')

        my_id = my_dict['id']
        i = arguments[0] + "." + my_id
        if i not in storage.all():
            print("** no instance found **")
        my_obj = storage.all()[i]

        for k_name, l_value in my_dict.items():
            setattr(my_obj, k_name, l_value)

        my_obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
