#!/usr/bin/python3
"""Module to search and update"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, after each
    line containing a specific string"""

    str = ""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            str = str + line
            if search_string in line:
                str = str + new_string
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str)
