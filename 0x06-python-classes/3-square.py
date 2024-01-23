#!/usr/bin/python3
"""A module for class Square"""


class Square:
    """The class Square"""

    def __init__(self, size=0):
        """Initializer or constructor of new object"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the area of Square"""

        return (self.__size**2)
