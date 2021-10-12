#!/usr/bin/python3
"""Creates a module to create a class and raises and exception"""


class BaseGeometry():
    """Class BaseGeometry with def area"""

    def area(self):
        raise Exception("area() is not implemented")
