#!/usr/bin/python3
"""The Module Defineing The Entry Point Of The Command_Interpreter

It is defineing one class, `HBNBCommand()`, which sub-classes of
the `cmd.Cmd` class.

"""

from models import storage
from models.base_model import BaseModel
from models.review import Review
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
import re
import cmd
import json

current_classes = {'BaseModel': BaseModel, 'User': User,
                   'Place': Place, 'Amenity': Amenity, 'City': City,
                   'State': State, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """The command interpreter, This class (HBNB)
      represents the command interpreter
    """

    prompt = "(hbnb) "

    def do_help(self, Arg):
        """handle help on command, type help <topic>.
        """
        return super().do_help(Arg)

    def do_EOF(self, line):
        """Inbuilt EOF_command.
        """
        print("")
        return True

    def do_quit(self, arg):
        """Quit command >>"exit".
        """
        return True

    def emptyline(self):
        """handle Override default "empty line && return" behaviour.
        """
        pass

    def do_create(self, arg):
        """Createing new instance.
        """
        args = arg.split()
        if not Validate_ClassName(args):
            return

        new_obj = current_classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, Arg):
        """Printing String Representation Of An_Instance.
        """
        Args = Arg.split()
        if not Validate_ClassName(Args, Check_Id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(Args[0], Args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        print(req_instance)

    def do_destroy(self, Arg):
        """Deleteing An_Instance BasedOn the Class_Name & Id.
        """
        Args = Arg.split()
        if not Validate_ClassName(Args, Check_Id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(Args[0], Args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return

        del instance_objs[key]
        storage.save()

    def do_all(self, Arg):
        """Printing String Representation Of All_Instances."""
        Args = Arg.split()
        all_objs = storage.all()

        if len(Args) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return
        if Args[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(str(v))
                  for _, v in all_objs.items() if type(v).__name__ == Args[0]])
            return

    def do_update(self, arg: str):
        """Updateing An_Instance BasedOn the Class_name & Id.
        """
        Args = arg.split(maxsplit=3)
        if not Validate_ClassName(Args, Check_Id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(Args[0], Args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return

        match_json = re.findall(r"{.*}", arg)
        if match_json:
            payload = None
            try:
                payload: dict = json.loads(match_json[0])
            except Exception:
                print("** invalid syntax")
                return
            for k, v in payload.items():
                setattr(req_instance, k, v)
            storage.save()
            return
        if not Validate_Attrs(Args):
            return
        first_attr = re.findall(r"^[\"\'](.*?)[\"\']", Args[3])
        if first_attr:
            setattr(req_instance, Args[2], first_attr[0])
        else:
            value_list = Args[3].split()
            setattr(req_instance, Args[2], Parse_Str(value_list[0]))
        storage.save()


def Validate_ClassName(Args, Check_Id=False):
    """Running Checks On Args to Validate Classname Entry.
    """
    if len(Args) < 1:
        print("** class name missing **")
        return False
    if Args[0] not in current_classes.keys():
        print("** class doesn't exist **")
        return False
    if len(Args) < 2 and Check_Id:
        print("** instance id missing **")
        return False
    return True


def Validate_Attrs(args):
    """Running Checks on Args to Validate Classname attributes & Values.
    """
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    if len(args) < 4:
        print("** value missing **")
        return False
    return True


def Is_Float(x):
    """Check if `x` is float!!
    """
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True


def Is_Int(x):
    """Check if `x` is Integer!!
    """
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


def Parse_Str(Arg):
    """Parse "Arg" to "int"& "float"
    | "String".
    """
    parsed = re.sub("\"", "", Arg)

    if Is_Int(parsed):
        return int(parsed)
    elif Is_Float(parsed):
        return float(parsed)
    else:
        return Arg


if __name__ == "__main__":
    HBNBCommand().cmdloop()
