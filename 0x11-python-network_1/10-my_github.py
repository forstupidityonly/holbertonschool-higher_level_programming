#!/usr/bin/python3
"""comment"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://api.github.com/user"
    response = requests.get(url, auth=(argv[1], argv[2]))
    print(response.json().git("id"))
