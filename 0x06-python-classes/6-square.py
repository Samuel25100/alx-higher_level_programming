#!/usr/bin/python3
"""A module for class Square"""


class Square:
    """The class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializer or constructor of new object"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrive the value of the attribute position"""
        return (self.__property)

    @position.setter
    def position(self, value):
        """Setter of the value to position attribute"""
        if (not isinstance(value, tuple)) or \
                len(value) != 2 or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return the area of Square"""
        return (self.__size**2)

    def my_print(self):
        """Print square using # symbol and in size of size"""
        if (self.__size != 0):
            for i in range(self.__position[1]):
                print("", end="")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
