#!/usr/bin/python3
"""the base class for rectangle and square"""
import json
import os


class Base:
    """for inheritence reasons"""
    __nb_objects = 0

    def __init__(self, id=None):
        """every object gets an id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionary to json string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json rep of dict saved to file"""
        if list_objs is None:
            list_objs = []
        file = cls.__name__ + ".json"
        empty_list = []
        for itr in list_objs:
            empty_list.append(itr.to_dictionary())
        with open(file, "w", encoding="UTF-8") as file:
            file.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """decode json"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """make an object"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ is "Rectangle":
            object = Rectangle(1, 1)
        elif cls.__name__ is "Square":
            object = Square(1)
        object.update(**dictionary)
        return (object)

    @classmethod
    def load_from_file(cls):
        """open file make dict other just empty dict"""
        if not os.path.isfile(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
