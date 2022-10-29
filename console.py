#!/usr/bin/python3
""" Console Module """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """ Entry point of the command interpreter"""
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User}

    def do_quit(self, command):
        """ Method to exit the console"""
        exit()

    def help_quit(self):
        """ the help documentation for quit  """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """ EOF to exit program """
        exit()

    def help_EOF(self):
        """ the help documentation for EOF """
        print("EOF command to exit the program")

    def emptyline(self):
        """ emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel """
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist")
            return
        new_cmd = HBNBCommand.classes[args]()
        print(new_cmd.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        new_input = args.partition(" ")
        clss_name = new_input[0]
        clss_id = new_input[2]
        if not clss_name:
            print("** class name missing **")
            return

        if clss_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not clss_id:
            print("** instance id missing **")
            return

        key = clss_name + "." + clss_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id """
        new_input = args.partition(" ")
        clss_name = new_input[0]
        clss_id = new_input[2]
        if not clss_name:
            print("** class name missing **")
            return

        if clss_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not clss_id:
            print("** instance id missing **")
            return

        key = clss_name + "." + clss_id
        try:
            del(storage._FileStorage__objects[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        listToPrint = []

        if args:
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for i, j in storage._FileStorage__objects.items():
                if i.split('.')[0] == args:
                    listToPrint.append(str(j))
        else:
            for i, j in storage._FileStorage__objects.items():
                listToPrint.append(str(i))

        print(listToPrint)

    def do_update(self, args):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        """
        new_input = args.split(" ")
        try:
            clss_name = new_input[0]
            clss_id = new_input[1]
            key = clss_name + "." + clss_id
            attr_name = new_input[2]
            attr_val = new_input[3]
        except:
            pass

        if not clss_name:
            print("** class name missing **")
            return

        if clss_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not clss_id:
            print("** instance id missing **")
            return
        if key not in storage._FileStorage__objects:
            print("** no instance found **")
            return

        if not attr_name:
            print("** attribute name missing **")
            return

        if not attr_val:
            print("** value missing **")
            return

        try:
            new_dict = storage._FileStorage__objects[key]
            new_dict.__dict__.update({attr_name: attr_val})
            storage.save()
        except KeyError:
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
