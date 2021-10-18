#!/usr/bin/python3
"""Module creates a Class Base"""


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
