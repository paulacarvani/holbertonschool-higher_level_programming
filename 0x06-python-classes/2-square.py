#!/usr/bin/python3
"""This module creates a class named square with a private atribute size 
    and diferent conditions"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Construct wit private parameter size and conditionals"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
