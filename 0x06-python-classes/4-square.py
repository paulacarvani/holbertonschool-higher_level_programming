#!/usr/bin/python3
"""This module creates a class named square with a private atribute size
    a public parameter area to calculates area with size
    uses a getter for size and setter to size with some conditions
    for type error and value error"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Construct wit private parameter size"""
        self.__size = size

    def area(self):
        """New construct with public parameters for calculates the area
        size elevates at 2"""
        return self.__size ** 2
    
    @property
    def size(self):
        """Getter for size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter for size with conditions"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
