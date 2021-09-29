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
    def position(self, position):
        """Setter for positions with conditions"""
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """public parameters for calculates the area size elevates at 2"""
        return self.__size ** 2

    def my_print(self):
        """Public parameter for print a square"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for i in range(self.__size):
                    print("#", end="")
                print("")
