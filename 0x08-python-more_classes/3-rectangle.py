#!/usr/bin/python3
"""Module that creates a class Rectangle with
private atribute width and height with his getter and setter
also with conditionals of typeerror and valuerror
Public instance method for calculates area and perimeter
Uses a print() and str() for a string representation"""


class Rectangle:
    """Class Rectangle"""
    def __init__(self, width=0, height=0):
        """Privates atributes"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        repr = ""
        if self.__width == 0 or self.__height == 0:
            return repr
        for i in range(self.__height):
            repr += ("#" * self.__width)
            if i is not self.__height -1:
                repr += "\n"
        return repr
