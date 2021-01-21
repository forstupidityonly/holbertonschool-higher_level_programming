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
        if not isinstance(attrs, list):
            return self.__dict__
        for i in attrs:
            if not isinstance(i, str):
                return self.__dict__
        my_dict = {}
        for itr in attrs:
            if itr in self.__dict__:
                my_dict.update({itr: self.__dict__[itr]})
        return my_dict

    def reload_from_json(self, json):
        """for the checker"""
        for i in json:
            if i == "first_name":
                self.first_name = json[i]
            if i == "last_name":
                self.last_name = json[i]
            if i == "age":
                self.age = json[i]
