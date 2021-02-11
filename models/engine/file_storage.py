#!/usr/bin/python3
"""
Module with FileStorage class
"""
import json
from models.base_model import BaseModel


class FileStorage():

    """ Class that serializes and deserializes JSON stuff """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns objects dict """
        return self.__objects

    def new(self, obj):
        """ Fills objects dict """
        self.__objects[str(obj.__class__.__name__ + "." + obj.id)] = obj

    def save(self):
        """ Serializes objects to JSON file """
        ob_dic = {}
        for k, v in self.__objects.items():
            ob_dic[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(ob_dic, f)

    def reload(self):
        """ Deserialize JSON file to objects """
        try:
            with open(self.__file_path, "r") as f:
                tmp = json.load(f)
            for item in tmp.values():
                cls = item["__class__"]
                del item["__class__"]
                self.new(eval(cls)(**item))
        except:
            pass
