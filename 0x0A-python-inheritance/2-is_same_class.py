#!/usr/bin/python3
"""Module for the function to compare if the object is exactly
an instance of the specified class"""


def is_same_class(obj, a_class):
    """Function to compare
    type of obj if is an instance
    of the a_class"""

    if type(obj) == a_class:
        return True
    else:
        return False
