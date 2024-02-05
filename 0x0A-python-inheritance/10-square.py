#!/usr/bin/python3
"""Class Square inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define Square."""

    def __init__(self, size):
        """Initialize size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
