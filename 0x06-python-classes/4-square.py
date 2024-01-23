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

    @property
    def size(self):
        """Retrive the value of the attribute size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter of the value to size attribute"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the area of Square"""

        return (self.__size**2)
