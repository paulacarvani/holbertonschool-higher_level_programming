#!/usr/bin/python3
"""Module creates a Class Base"""
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Construct"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
