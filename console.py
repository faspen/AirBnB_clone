#!/usr/bin/python3
""" Module with console class """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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
                k = args[0] + "." + args[1]
                if k in list(models.storage.all().keys()):
                    del models.storage.all()[k]
                    models.storage.save()
                else:
                    HBNBCommand.error_helper(4)
            else:
                HBNBCommand.error_helper(2)

    def do_all(self, items):
        """Print string representation of all instances"""
        new_list = []
        args = items.split()
        warehouse = models.storage.all()

        if len(args) == 0:
            for inst in warehouse.keys():
                obj = warehouse[inst]
                new_list.append(str(obj))
            print(new_list)
        else:
            if HBNBCommand.validate(args[0]):
                for inst in warehouse.keys():
                    if (args[0] in inst):
                        obj = warehouse[inst]
                        new_list.append(str(obj))
                print(new_list)
            else:
                HBNBCommand.error_helper(2)

    def do_update(self, items):
        """Update an instance"""
        args = items.split()
        qargs = items.split('"')
        warehouse = models.storage.all()

        if len(args) is 0:
            HBNBCommand.error_helper(1)
        elif (HBNBCommand.validate(args[0])):
            if not issubclass(eval(args[0]), BaseModel):
                HBNBCommand.error_helper(2)
            else:
                if len(args) is 1:
                    HBNBCommand.error_helper(3)
                else:
                    k = args[0] + "." + args[1]
                    if k in warehouse:
                        if len(args) is 2:
                            HBNBCommand.error_helper(5)
                        else:
                            if len(qargs) is 1:
                                HBNBCommand.error_helper(6)
                            else:
                                setattr(
                                    warehouse[k],
                                    str(args[2]),
                                    str(qargs[1])
                                )
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
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
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
