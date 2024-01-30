#!/usr/bin/python3
"""Add integer return result."""


def add_integer(a, b=98):
    """Add integer a and b."""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    num = int(a) + int(b)
    return num
