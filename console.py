#!/usr/bin/python3
"""command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class cmd """
    prompt = "(hbnb)"

    def do_quit(self, args):
        """quit interpreter"""
        return True

    def do_EOF(self, args):
        """End of file"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, arg):
        """creating"""
        arguments = args.split()
        if not self.class_verification(args):
            return

        instance = eval(str(arsg[0] + '()'))
        if not isinstance(instance, BaseModel):
            return
        instance.save()
        print(instance.id)

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
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        models.storage.delete(objects[string_key])
        models.storage.save()

    def do_all(self, args):

    def do_update(self, line):

if __name__ == '__main__':
    HBNBCommand().cmdloop()
