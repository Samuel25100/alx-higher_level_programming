#!/usr/bin/python3
"""Print square function."""


def print_square(size):
    """Print square using char '#' in size argument size."""
    if ((not isinstance(size, int)) or
            (isinstance(size, float) and (size < 0))):
        raise TypeError("size must be an integer")
    if not (size >= 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
