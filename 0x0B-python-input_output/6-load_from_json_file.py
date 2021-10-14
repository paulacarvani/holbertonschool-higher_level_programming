#!/usr/bin/python3
"""Module that creates at objetc with json"""


import json


def load_from_json_file(filename):
    """ function that creates an Object from a JSON file"""

    with open(filename, mode="r", encoding="utf-8") as my_file:
        return json.loads(my_file.read())
