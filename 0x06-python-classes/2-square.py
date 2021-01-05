#!/user/bin/python3
"""my square mod"""
class Square:
    """def a square"""
    def __init__(self, size=0):
        """
            make square
            size = side
            raise int and 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
