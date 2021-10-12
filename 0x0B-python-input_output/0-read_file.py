#!/usr/bin/python3
"""
Module that creates a function for read and print a txt file
"""


def read_file(filename=""):
    """Function that receives a text file,
    reads in UTF8 and prints in stdout"""

    with open(filename, encoding="UTF8") as myfile:
        print(myfile.read(), end="")
        myfile.close()
