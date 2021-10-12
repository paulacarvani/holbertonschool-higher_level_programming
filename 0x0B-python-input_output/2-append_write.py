#!/usr/bin/python3
"""Module to append a text in file"""


def append_write(filename="", text=""):
    """Function that appends a text in a text file and
    return the number of char written"""

    with open(filename, mode="a", encoding="UTF8") as myfile:
        return (myfile.write(text))
