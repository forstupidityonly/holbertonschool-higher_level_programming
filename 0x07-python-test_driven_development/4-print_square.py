#!/usr/bin/python3
"""text identification module"""


def print_square(size):
    """
        print square of size
    """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        print("", end="")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
