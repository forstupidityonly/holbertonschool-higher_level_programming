#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    if (argv[1] is not None and argv[2] is not None):
        url = argv[1]
        email = argv[2]
        values = {"email": email}
        data = urllib.parse.urlencode(values)
        data = query_string.encode("ascii")

        with urllib.request.urlopen(url, data) as response:
            response_text = response.read()
            response_text = response_text.decode("UTF-8")
            print(response_text)
