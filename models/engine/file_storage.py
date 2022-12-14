#!/usr/bin/python3
"""
Module that defines a classthat serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json


class FileStorage:
    """storage managing class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns currently storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """serializes objects to JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            tmp = {}
            tmp.update(FileStorage.__objects)
            for key, val in tmp.items():
                tmp[key] = val.to_dict()
            json.dump(tmp, f)

    def reload(self):
        """ deserializes JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        cls = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'Place': Place,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            tmp = {}
            with open(FileStorage.__file_path, 'r') as f:
                tmp = json.load(f)
                for key, val in tmp.items():
                    self.all()[key] = cls[val['__class__']](**val)
        except FileNotFoundError:
            pass
