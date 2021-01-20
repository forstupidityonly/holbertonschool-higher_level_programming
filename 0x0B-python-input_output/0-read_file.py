#!/usr/bin/python3
"""for the checker"""


def read_file(filename=""):
    """for the checker"""
    with open(filename, "r") as file:
        print(file.read(), end="")
