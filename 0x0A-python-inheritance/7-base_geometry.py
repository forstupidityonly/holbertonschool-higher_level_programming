#!/usr/bin/python3
"""base geometry"""


class BaseGeometry:
    """num 6"""

    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if(not isinstance(value, int)):
            raise TypeError(name + " must be an integer")
        if(value <= 0):
            raise ValueError(name + " must be greater than 0")
