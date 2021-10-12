#!/usr/bin/python3
"""Module to create a class and import another class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square with atributes from rectangle"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Print a string"""
        return ("[Square] {}/{}".format(str(self.__size), str(self.__size)))
