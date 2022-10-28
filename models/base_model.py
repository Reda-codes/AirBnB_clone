#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for AirBnB clone"""
import uuid
from datetime import datetime

class BaseModel:
    """base class"""
    def __init__(self):
        """initializing a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
    def __str__(self):
        return '[BaseModel] (' + str(self.id ) + ')'+ ' ' + str(self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        newDict = {}
        newDict.update(self.__dict__)
        newDict.update({'__class__':
            (str(type(self)).split('.')[-1]).split('\'')[0]})
        newDict['created_at'] = self.created_at.isoformat()
        newDict['updated_at'] = self.updated_at.isoformat()
        return newDict
