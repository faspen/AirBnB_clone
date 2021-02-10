#!/usr/bin/python3
"""
BaseModel is the base class for all other classes
"""
from datetime import datetime
import models
import uuid


class BaseModel():

    """ Defines common elements for future classes """

    def __init__(self):
        """ Constructor for base class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Print string representation of object """
        string = "[" + str(self.__class__.__name__) + "]"
        string += "(" + str(self.id) + ")"
        string += str(self.__dict__)
        return string

    def save(self):
        """ Updates 'updated_at' with current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return dict containing all keys/values of __dict__ """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
