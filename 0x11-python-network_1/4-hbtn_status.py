#!/usr/bin/python3
"""use requests"""
import requests


if __name__ == "__main__":
    data = requests.get("https://intranet.hbtn.io/status")
    content = data.text
    print("Body response:\n\t- type: " + str(type(content)))
    print("\t- content: " + str(content))
