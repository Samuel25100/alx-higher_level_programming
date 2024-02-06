#!/usr/bin/python3
"""Read a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """Read text file from filename."""
    with open(filename, 'r') as f:
        for line in f:
            print(line, end="")
    f.close()
