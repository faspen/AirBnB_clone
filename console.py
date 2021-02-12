#!/usr/bin/python3
""" Module with console class """
import cmd
from models.base_model import BaseModel
import sys
import models


class HBNBCommand(cmd.Cmd):

    """ Command line interpreter class
    """
    prompt = "(hbnb) "

    def do_create(self, args):
        """Create method instance """
        if len(args) is 0:
            HBNBCommand.error_helper(1)
        else:
            toks = args.split()
            if HBNBCommand.validate(toks[0]):
                new = eval(toks[0])(toks[1:])
                print(new.id)
                new.save()
            else:
                HBNBCommand.error_helper(2)

    def do_show(self, items):
        """Show string representation of instance """
        args = items.split()

        if len(args) is 0:
            HBNBCommand.error_helper(1)
        elif len(args) is 1:
            HBNBCommand.error_helper(3)
        else:
            if HBNBCommand.validate(args[0]):
                models.storage.reload()
                k = args[0] + "." + args[1]
                if k in list(models.storage.all().keys()):
                    print(models.storage.all()[k])
                else:
                    HBNBCommand.error_helper(4)
            else:
                HBNBCommand.error_helper(2)

    def do_destroy(self, items):
        """Destroy an instance """
        args = items.split()

        if len(args) is 0:
            HBNBCommand.error_helper(1)
        elif len(args) is 1:
            HBNBCommand.error_helper(3)
        else:
            if HBNBCommand.validate(args[0]):
                models.storage.reload()
                k = args[0] + "." + args[1]
                if k in list(models.storage.all().keys()):
                    del models.storage.all()[k]
                    models.storage.save()
                else:
                    HBNBCommand.error_helper(4)
            else:
                HBNBCommand.error_helper(2)

    def do_quit(self, *args):
        """Quit command to exit the program """
        return True

    def do_EOF(self, *args):
        """End of file """
        print("")
        return True

    def emptyline(self):
        """ Do nothing on empty line """
        pass

    def validate(arg_pass):
        """ Check if class is valid """
        classes = [
            "BaseModel"
        ]
        if arg_pass in classes:
            return True
        else:
            return False

    def error_helper(err_num):
        """ Handle errors """
        if err_num is 1:
            print("** class name missing **")
        elif err_num is 2:
            print("** class doesn't exist **")
        elif err_num is 3:
            print("** instance id missing **")
        elif err_num is 4:
            print("** no instance found **")
        elif err_num is 5:
            print("** attribute name missing **")
        else:
            print("** value missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
