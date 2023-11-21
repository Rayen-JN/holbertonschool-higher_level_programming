#!/usr/bin/python3
"""
module Base class
"""
import json


class Base:
    """
    This class will be the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = 0
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the dictionary representation of json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        return an instance with all attributes
        """
        if cls.__name__ == "Square":
            dummy = cls(size=99)
        elif cls.__name__ == "Rectangle":
            dummy = cls(height=5, width=5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                cont = f.read()
                list = cls.from_json_string(cont)
                instan_l = []
                for dict in list:
                    instan = cls.create(**dict)
                    instan_l.append(instan)
                return instan_l
        except FileNotFoundError:
            return []
