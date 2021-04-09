#!/usr/bin/pyhon3
"""comment"""
import urllib.error
import urllib.request 
from sys import argv


if __name__ == "__main__":
    if argv[1] is not None:
        try:
            with urllib.request.urlopen(argv[1]) as response:
                body = response.read()
                body = body.decode("UTF-8")
                print(body)
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
