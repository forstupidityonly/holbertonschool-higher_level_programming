#!/usr/bin/python3
"""my square"""
class Square:
    """def a square"""
    def __init__(self, size=0, position=(0, 0)):
        """
            set size and pos
        """
        self.__size = size
        self.__position = position

    """def area"""
    def area(self):
        return self.__size**2
    """get size"""
    @property
    def size(self):
        return self.__size
    """
       set size
       raise int and 0 checks
    """
    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be in integer")
        if value < 0:
            raise ValueError("size must be >= 0")
    """get pos"""
    @property
    def position(self, value):
        return self.__position
    """set pos
       tuple raises
    """
    @position.setter
    def position(self, value):
        self.__postition = value
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tulpe of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tulpe of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tulpe of 2 positive integers")
    """to print"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print("")
