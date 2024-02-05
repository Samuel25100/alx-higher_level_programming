#!/usr/bin/python3
"""Adds a new attribute to an object if it’s possible."""

def add_attribute(a, b, c):
    """Adds a new attribute to an object if it’s possible."""
    if not hasattr(a, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(a, b, c)
