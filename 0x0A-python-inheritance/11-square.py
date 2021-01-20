#!/usr/bin/python3
"""stuff for checker"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """stuff for checker"""

    def __init__(self, size):
        """stuff for checker"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """stuff for checker"""
        return("[Square] {}/{}".format(self.__size, self.__size))
