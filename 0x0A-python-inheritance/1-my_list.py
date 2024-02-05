#!/usr/bin/python3
"""Function class MyList that inherits from list."""


class MyList(list):
    """Class Mylist inherit for list."""

    def print_sorted(self):
        """Print the sorted list  in ascending order."""
        print(sorted(self))
