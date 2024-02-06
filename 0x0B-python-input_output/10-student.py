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
        """Retrieve a dictionary representation of a Student."""
        if attrs is None:
            return self.__dict__
        dic = {}
        for i in attrs:
            if i in self.__dict__.keys():
                dic[i] = self.__dict__[i]
        return dic
