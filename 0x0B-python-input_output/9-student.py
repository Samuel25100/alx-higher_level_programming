#!/usr/bin/python3
"""Define class Student."""


class Student:
    """Repersent class Student."""

    def __init__(self, first_name, last_name, age):
        """Init initalize attribute."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student."""
        return self.__dict__
