#!/usr/bin/python3
"""This module creates a class named square with a private atribute size"""


class Square:
    """Square Class"""
    def __init__(self, size):
        """Construct wit private parameter size"""
        self.__size = size
