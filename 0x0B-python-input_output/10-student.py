#!/usr/bin/python3
"""for the checker"""


class Student:
    """for the checker"""

    def __init__(self, first_name, last_name, age):
        """for the checker"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """for the checker"""
        return self.__dict__
