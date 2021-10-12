#!/usr/bin/python3
"""Module that creates a function to write ina text file"""


def write_file(filename="", text=""):
    """This function open a text files and writes replacing
    the text in the file, returns the number of char in the file"""

    with open(filename, mode="w", encoding="UTF8") as filewrite:
        return(filewrite.write(text))
