#!/usr/bin/python3
#!/usr/bin/python3
""" Console Module """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Entry point of the command interpreter"""
    prompt = '(hbnb)'

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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
