#!/usr/bin/python3
""" Module to import another class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "Inheritance from class BaseGeometry to class Rectangle"

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Prints a str"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height )
