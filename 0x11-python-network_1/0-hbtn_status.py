#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
from urllib import request
from urllib import error


try:
	with request.urlopen('https://intranet.hbtn.io/status') as f:
		response = f.read()
		print("Body response:")
		print("\t- type: {}".format(type(response)))
		print("\t- content: {}".format(response))
		print("\t- utf8 content: {}".format(response.decode('utf-8')))
except urllib.error.URLError as er:
	print(er)
