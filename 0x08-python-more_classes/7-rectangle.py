#!/usr/bin/python3
"""empty class Rectangle that defines a rectangle."""


class Rectangle:
    """Class of rectangle of char '#' with width and height."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Class rectangle initializer."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the rectangle using str() or print() function."""
        if self.__height == 0 and self.__width == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect = rect + str(self.print_symbol)
            rect = rect + '\n'
        return rect[:-1]

    def __repr__(self):
        """Repr use to allow call using repr() and evac()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Del print <bye rectangle...>."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
