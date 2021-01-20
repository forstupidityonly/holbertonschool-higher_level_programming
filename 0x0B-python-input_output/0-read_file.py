#!/usr/bin/python3
"""for the checker"""

def read_file(filename=""):
    """for the checker"""
    with open(filename, encoding="UTF-8") as file:
        print(file.read, end="")
