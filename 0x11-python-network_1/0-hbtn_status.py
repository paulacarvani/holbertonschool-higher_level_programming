#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as f:
        response = f.read()
        print("Body response:")
        print("    - type: {}".format(type(response)))
        print("    - content: {}".format(response))
        print("    - utf8 content: {}".format(response.decode('utf-8')))
