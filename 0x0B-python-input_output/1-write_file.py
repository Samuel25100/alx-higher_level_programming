#!/usr/bin/python3
"""Write a string to a text file (UTF8), returns the num of char."""


def write_file(filename="", text=""):
    """Write on file 'filename' the string 'text'."""
    with open(filename, 'w', encoding="UTF8") as f:
        num = f.write(text)
    return (num)
