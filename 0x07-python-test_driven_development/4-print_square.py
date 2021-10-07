#!/usr/bin/python3
"""Module that creates a function for
print a square with the character #"""


def print_square(size):
    """Function for prints a square where
    size is the size length of the square
    size must be a integer and greater than 0
    size can´t be a float"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
