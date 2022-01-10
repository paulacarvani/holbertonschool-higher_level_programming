#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv


if __name__ == "__main__":
    letter = ""
    url = "http://0.0.0.0:5000/search_user"
    try:
        letter = argv[1]
    except IndexError:
        pass

    response = requests.post(url, data={'q': letter})

    try:
        response = response.json()
        if (response):
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
