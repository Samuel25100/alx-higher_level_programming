#!/usr/bin/python3
"""Define class Student."""


class Student:
    """Repersent class Student."""

    def __init__(self, first_name, last_name, age):
        """Init initalize attribute."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve the filtred attributes of dictionary."""
        if attrs is None:
            return self.__dict__
        dic = {}
        for i in attrs:
            if i in self.__dict__.keys():
                dic[i] = self.__dict__[i]
        return dic

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance."""
        if 'first_name' in json:
            self.first_name = json['first_name']
        if 'last_name' in json:
            self.last_name = json['last_name']
        if 'age' in json:
            self.age = json['age']
