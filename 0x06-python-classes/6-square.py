#!/usr/bin/python3
"""This module creates:
    - a class named square with a private atribute size
    - a public parameter area to calculates area with size
    - uses a getter for size and setter to size with
    some conditions for type error and value error
    - Public parameters for print a square with #
    - Private parameter called position
    - Getter and setter for position
    - Publica parameter for print a square"""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """Construct wit private parameter size and position"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for positions with conditions"""
        if type(value) != tuple or len(value) != 2 or \
           not all([type(i) == int for i in value]) or \
           not all([i >= 0 for i in value]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """public parameters for calculates the area size elevates at 2"""
        return self.__size ** 2

    def my_print(self):
        """Public parameter for print a square"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
