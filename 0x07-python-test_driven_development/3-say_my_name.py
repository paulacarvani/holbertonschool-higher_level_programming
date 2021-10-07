#!/usr/bin/python3
"""Module to creates a function for
print the first and last name
only if there are strings"""


def say_my_name(first_name, last_name=""):
    """Function to print first and las name
    only when the objects are string"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
