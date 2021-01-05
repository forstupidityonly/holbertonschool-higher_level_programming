#!/usr/bin/python3
"""my square mod"""
class Square:
    """def the squaare"""
    def __init__(self, size=0):
        """
            make it
            make area
            use propertey to get size
            use serrter to set size
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
        if not isinstance(value, int):
            raise TypeError("size must be in integer")
        if value < 0:
            raise ValueError("size must be >= 0")
