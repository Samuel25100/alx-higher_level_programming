#!/usr/bin/python3
"""Class square."""
from models.rectangle import Rectangle


class Square(Rectangle): 
    """Define square and it inherit from a class rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer of square class."""
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        """Override the __str__ method to return the following."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        "Width getter."
        return(self.width)

    @size.setter
    def size(self, size):
        """Setter for size."""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update all attributes."""
        if args:
            ln = len(args)
            if ln >= 1:
                self.id = args[0]
            if ln >= 2:
                self.size = args[1]
            if ln >= 3:
                self.x = args[2]
            if ln >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
