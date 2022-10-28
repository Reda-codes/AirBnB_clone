#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for AirBnB clone"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """base class"""
    def __init__(self, *args, **kwargs):
        """initializing a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """method returns the string representation of the object"""
        return '[BaseModel] (' + str(self.id) + ')' + ' ' + str(self.__dict__)

    def save(self):
        """Updates updated_at to a new time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        newDict = {}
        newDict.update(self.__dict__)
        newDict.update({'__class__':
                        (str(type(self)).split('.')[-1]).split('\'')[0]})

        newDict['created_at'] = self.created_at.isoformat()
        newDict['updated_at'] = self.updated_at.isoformat()
        return newDict
