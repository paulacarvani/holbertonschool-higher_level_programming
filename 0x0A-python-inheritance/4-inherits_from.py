#!/usr/bin/python3
"""Module for function def inherits_from(obj, a_class)"""


def inherits_from(obj, a_class):
    """ function that returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False"""

    return isinstance(obj, a_class) and not type(obj) == a_class
