#!/usr/bin/python3
""" Module with console class """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import sys


class HBNBCommand(cmd.Cmd):

    """ Command line interpreter class
    """
    prompt = "(hbnb) "

    def do_quit(self, *args):
        """ Quit the console """
        return True

    def do_EOF(self, *args):
        """ End of file """
        print("")
        return True

    def emptyline(self):
        """ Do nothing on empty line """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
