#!/usr/bin/python3
"""my square mod"""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """
            make a square
            make a area
            use propery to get size
            use setter to set value
            raise int and 0 check
        """
        self.__size = size

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be in integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """to print"""
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print("")
