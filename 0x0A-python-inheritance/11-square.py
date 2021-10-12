#!/usr/bin/python3
"""Module to create a class and import another class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square with atributes from rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Prints a String"""
        return "[Square] {}/{}".format(self.__size, self.__size)
