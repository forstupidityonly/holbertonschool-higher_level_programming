#!/usr/bin/pyhton3
"""my square mod"""
class Square:
    """deff the square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            """make it 
               args size of sueare
               raise int and pos or 0
            """
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
"""area of square"""
    def area(self):
        return self.__size ** 2
