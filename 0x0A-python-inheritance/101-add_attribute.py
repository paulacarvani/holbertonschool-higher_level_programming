#!/usr/bin/python3
"""Task Advanced"""


def add_attribute(ob, name, value):
    if hasattr(ob, name) or not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob, name, value)