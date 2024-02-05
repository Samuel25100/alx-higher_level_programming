#!/usr/bin/python3
"""Method is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Return True if the object is an instance of, else False."""
    if isinstance(obj, a_class):
        return True
    return False
