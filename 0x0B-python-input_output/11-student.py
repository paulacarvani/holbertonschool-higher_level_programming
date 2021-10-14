#!/usr/bin/python3
"""Module with the class Student"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        Newdict = {}
        for i in attrs:
            try:
                Newdict[i] = self.__dict__[i]
            except:
                pass
        return Newdict

    def reload_from_json(self, json):
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
