#!/usr/bin/python3
"""comment"""
from sys import argv
import requests


if __name__ == "__main__":
    if argv[1] is not None and argv[2] is not None:
        url = argv[1]
        email = argv[2]
        data = {'email': email}
        info = requests.post(url, data)
        value = info.text
        print(str(value))
