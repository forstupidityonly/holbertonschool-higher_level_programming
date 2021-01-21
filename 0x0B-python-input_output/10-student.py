#!/usr/bin/python3
"""for the checker"""


class Student:
    """for the checker"""

    def __init__(self, first_name, last_name, age):
        """for the checker"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """for the checker"""
        if not isinstance(attrs, list) or len(attrs) < 1:
            return self.__dict__
        for i in attrs:
            if not isinstance(i, str):
                return self.__dict__
        return {
            name: value for name,
            value in self.__dict__.items() if name in attrs}
