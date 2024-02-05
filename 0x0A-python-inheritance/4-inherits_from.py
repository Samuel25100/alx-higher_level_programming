#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Return True if object is instance of a class that inherited."""
    if (issubclass(type(obj), a_class)) and (type(obj) is not a_class):
        return True
    return False
