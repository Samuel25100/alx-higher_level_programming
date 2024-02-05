#!/usr/bin/python3
"""Class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Area of base geometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the attributes value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
