#!/usr/bin/python3
"""stuff for checker"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """stuff for checker"""

    def __init__(self, width, height):
        """stuff for checker"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
