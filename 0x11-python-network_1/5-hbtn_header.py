#!/usr/bin/python3
"""comment"""
import requests
from sys import argv


if __name__ == "__main__":
    data = requests.get(argv[1])
    header = data.headers
    print(header.get("X-Request-Id"))
