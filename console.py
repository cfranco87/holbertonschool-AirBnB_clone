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

if __name__ == '__main__':
        HBNBCommand().cmdloop()
