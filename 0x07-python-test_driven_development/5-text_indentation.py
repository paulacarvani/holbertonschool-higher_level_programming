#!/usr/bin/python3
"""Module that creates a function for
prints a text with 2 new lines after each
of these characters: ., ? and :"""


def text_indentation(text):
    """Function to replace a special characters with two spaces
    when the text received is a str"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    a = text.replace(". ", "."'\n\n').replace("? ", "?"'\n\n').replace(": ", ":"'\n\n')

    print(a)