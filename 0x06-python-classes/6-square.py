#!/usr/bin/python3
"""A module for class Square"""


class Square:
    """The class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializer or constructor of new object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if ((not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position))):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
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
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter of the value to position attribute"""
        if ((isinstance(value, tuple) is not True) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
            print("Hey There")
        else:
            self.__position = value

    def area(self):
        """Return the area of Square"""
        return (self.__size**2)

    def my_print(self):
        """Print square using # symbol and in size of size"""
        if (self.__size != 0):
            if (self.__position[1] > 0):
                print("")
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
