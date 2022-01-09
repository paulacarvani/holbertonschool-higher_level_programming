#!/usr/bin/python3
""" Takes a URL and return the X-Request-Id"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as ID:
        print(ID.headers.get('X-Request-Id'))
