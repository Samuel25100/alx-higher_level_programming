#!/usr/bin/python3
"""Have method is_same_class."""


def is_same_class(obj, a_class):
    """Return True if the object "obj"is an instance of the class."""
    if type(obj) is a_class:
        return True
    else:
        return False
