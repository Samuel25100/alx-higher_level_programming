#!/usr/bin/python3
"""Class base."""
import json
import os


class Base:
    """It is base of all class of this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialzer of class base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string rep of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string rep of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])
                f.write(list_dicts)

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON string representation json_string."""
        if json_string is None or json_string == []:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + ".json"
        list_tmp = []

        if os.path.exists(filename):
            with open(filename, 'r') as f:
                list_f = cls.from_json_string(f.read())
                for i in list_f:
                    list_tmp.append(cls.create(**i))
        return (list_tmp)
