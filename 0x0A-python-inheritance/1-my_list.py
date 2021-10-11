#!/usr/bin/python3
"""Module that creates a Class that inherits from list of another file
and sort the list created"""


class MyList(list):
    """Class that inherits from class list"""
    def print_sorted(self):
        print(sorted(self))
