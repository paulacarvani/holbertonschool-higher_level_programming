#!/usr/bin/python3
""" Takes a URL and return the X-Request-Id"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    ID = requests.get(url)
    print(ID.headers.get('X-Request-Id'))
