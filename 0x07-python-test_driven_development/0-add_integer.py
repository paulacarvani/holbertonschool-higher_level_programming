#!/usr/bin/python3
"""Module to add two args
    arg a + arg b
    Return a + b"""


def add_integer(a, b=98):
    """Function to add two integers"""
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if not type(a) is int:
        raise TypeError("a must be an integer")
    if not type(b) is int:
        raise TypeError("b must be an integer")
    return a + b