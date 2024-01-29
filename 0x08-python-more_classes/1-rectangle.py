#!/usr/bin/python3
"""empty class Rectangle that defines a rectangle."""


class Rectangle:
    """Class of rectangle of char '#' with width and height."""

    def __init__(self, width=0, height=0):
        """Class rectangle initializer."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width of the rectangle retriver."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Width of the rectangle setter."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height of the rectangle retriver."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Height of the rectangle setter."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
