#!/usr/bin/python3
""" Module to import another class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """New class Square inheritance from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
