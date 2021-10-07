#!/usr/bin/python3
"""Module to add two args
    arg a + arg b
    if a or b are float change to int
    ir a or b are not int or floar raise TypeError
    Return a + b"""


def add_integer(a, b=98):
    """Function to add two integers
    arg a and arg b
    return a + b"""
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if not type(a) is int:
        raise TypeError("a must be an integer")
    if not type(b) is int:
        raise TypeError("b must be an integer")
    return a + b
